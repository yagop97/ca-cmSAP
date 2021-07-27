import tabula
import re

url = r"C:\Users\ypajarino\Projects\2021.04.27 CARGA MASIVA SAP\2021.05\NDA-CGP-2289-VIAMONTE1.pdf"
def doc_conceptos (url):
    df = tabula.read_pdf(url,pages=1,multiple_tables=False,area=[320,20,510,480]) # 440
    df = df[0]
    textos = []
    for y in range(df.shape[0]):
        texto = ""
        for x in range(df.shape[1]):
            texto += str(df.iloc[y,x]) + " "
        textos.append(texto.lower())
    docs = {}
    conceptos = {"total":0,"neto gravado":0,"no gravado":0}
    regex = ["(iva).*(\d{2},\d{2}) %", "(iibb\s*\w*).*(\d{1,2},\d{2}) %", "(perc. iva).*(\d{1,2},\d{2}) %"]
    
    for texto in textos:
        texto = texto.replace("percepción", "perc.")
        texto = texto.replace("pcia. ", "")
        texto = texto.replace("  ", " ")
        for reg in regex:
            find = re.findall(reg, texto)
            if len(find) > 0:
                if find[0][0] == "iva":
                    con = find[0][0] + " " + find[0][1]
                    conceptos[con] = float(find[0][1].replace(",","."))/100
                else:
                    conceptos[find[0][0]] = float(find[0][1].replace(",","."))/100

    df = tabula.read_pdf(url,pages=1,multiple_tables=False,area=[20,350,55,570])
    df = df[0]
    string = df.values[0][0]
    nro_doc = re.findall(".*(\d{4}-\d{8})", string)[0]
    docs["nro_doc"] = nro_doc

    df = tabula.read_pdf(url,pages=1,multiple_tables=False,area=[235,15,255,250])
    df = df[0]
    conceptos["texto"] = df.columns[0]

    docs["datos"] = conceptos
    return docs


