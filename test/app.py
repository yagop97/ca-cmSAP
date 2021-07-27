import pandas as pd
import re
import tabula
from datetime import datetime
from read_pdf import doc_conceptos
import os
import numpy as np

cwd = os.getcwd()

url_afip = os.path.join(cwd, r"Mis Comprobantes Emitidos - CUIT 30657864281.xlsx")
afip = pd.read_excel(url_afip,skiprows=1)

url_clientes = os.path.join(cwd,r"CLIENTES.xlsx")
clientes = pd.read_excel(url_clientes,dtype={"CUIT":str})

url_indicadores = os.path.join(cwd,r"INDICADORES.xlsx")
indicadores = pd.read_excel(url_indicadores)

m = re.findall('CUIT (\d{11})', url_afip)
m = m[0]
if m == "30657864281":
    soc = "0070"
else:
    soc = "0080"

tipo_docs = {1:"DR", 2:"DD", 3:"DC", 6:"DR", 7:"DD"}
monedas = {"$":"ARS"}
debe_haber = {"DR":["01","50"],"DC":["11","40"],"DD":["01","50"]}

conceptos = {}
carpeta_docs = os.path.join(cwd, "docs")
dirs = os.listdir(carpeta_docs)
for doc in dirs:
    print("Leyendo doc: " + doc)
    url = os.path.join(carpeta_docs, doc)
    datos_doc = doc_conceptos(url)
    conceptos[datos_doc["nro_doc"]] = datos_doc["datos"]

empty_datos = {"texto":""}

docs = []
for x in range(afip.shape[0]):
    nro_doc = str(afip.loc[x,"Punto de Venta"]).zfill(4) + "-" + str(afip.loc[x,"Número Desde"]).zfill(8)
    try:
        datos = conceptos[nro_doc]
        datos["total"] = float(afip.loc[x,"Imp. Total"])
        if afip.loc[x,"Imp. Neto Gravado"] == 0:
            datos["no gravado"] = float(afip.loc[x,"Imp. Neto No Gravado"])
            neto = 1
            datos["neto gravado"] = 0
        else:
            datos["no gravado"] = float(afip.loc[x,"Imp. Neto No Gravado"]) / float(afip.loc[x,"Imp. Neto Gravado"])
            neto = float(afip.loc[x,"Imp. Neto Gravado"])
            datos["neto gravado"] = 1
    except:
        datos = empty_datos
    keys = list(datos.keys())
    keys.remove("texto")
    for y in keys:
        data = {}
        data["Sociedad"] = soc
        data["Fecha Doc"] = afip.loc[x,"Fecha"].replace("/","")
        data["Tipo Doc"] = tipo_docs[int(afip.loc[x,"Tipo"][0])]
        data["Fecha Cont."] = data["Fecha Doc"]
        data["Moneda"] = monedas[afip.loc[x,"Moneda"][0]]
        data["Tipo Cambio"] = afip.loc[x,"Tipo Cambio"]
        data["Nro Factura"] = nro_doc.replace("-",afip.loc[x,"Tipo"][-1])
        data["Texto"] = datos["texto"]
        if y == "total":
            data["Clave Cont."] = debe_haber[data["Tipo Doc"]][0]
            try:
                nro_sap = clientes.loc[clientes["CUIT"] == str(afip.loc[x,"Nro. Doc. Receptor"])[:-1],"NUM CLIENTE SAP"].values[0]
            except:
                nro_sap = str(afip.loc[x,"Nro. Doc. Receptor"])
            data["Cuenta"] = nro_sap
            data["Importe"] = datos["total"]
            data["Ind.Imp"] = "**"
            data["Ce.Benef."] = ""
            data["Localidad"] = ""
            data["Solicitante"] = ""
            docs.append(data)
        else:
            data["Clave Cont."] = debe_haber[data["Tipo Doc"]][1]
            if y in ["neto gravado", "no gravado"]:
                data["Cuenta"] = ""
                data["Importe"] = datos[y] * neto
                data["Ind.Imp"] = ""
            else:
                data["Cuenta"] = indicadores.loc[(indicadores["concepto"] == y) & (indicadores["alicuota"] == datos[y]), "cuenta"].values[0]
                data["Importe"] = datos[y] * neto
                data["Ind.Imp"] = indicadores.loc[(indicadores["concepto"] == y) & (indicadores["alicuota"] == datos[y]), "indicador"].values[0]
            data["Ce.Benef."] = ""
            data["Localidad"] = ""
            data["Solicitante"] = ""
            docs.append(data)

df = pd.DataFrame(docs)
df.drop(df[df["Importe"] == 0].index, inplace = True)

control = []
rows = df.shape[0]
c = 0
for x in range(rows):
    ind = df.iloc[x,11]
    try:
        next = df.iloc[(x+1),11]
    except:
        next = "**"
    if ind == "**":
        control.append("")
        c = df.iloc[x,10]
    elif next == "**":
        c -= df.iloc[x,10]
        if abs(c) < 0.1:
            control.append("Ok")
        else:
            control.append("Error")
    else:
        c -= df.iloc[x,10]
        control.append("")

a = np.asarray(control)
df["Control"] = a   

df.to_excel("salida.xlsx",index=False,float_format="%.2f")
print("Excel exportado")

