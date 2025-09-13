import csv
import xlrd
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom



def read_csv():
    with open('subvenciones.csv',encoding='utf-8') as fichero_csv:
        dict_lector = csv.DictReader(fichero_csv)
        print(dict_lector.fieldnames[0])
        asocs = {}
        print(asocs)
        total = 0
        for line in dict_lector:
            centro = line['Asociación']
            subvencion = float(line['Importe'])
            total += subvencion
            #Sum the subsidies for each association
            asocs[centro] = asocs.get(centro, 0) + subvencion
        assert total == sum(asocs.values())
        print(asocs)

def add_columns():
    with open('subvenciones.csv', encoding='utf-8') as fich_lect, \
        open('subvenciones_esc.csv', 'w', encoding='utf-8') as fich_escr:
        dict_lector = csv.DictReader(fich_lect)
        campos = dict_lector.fieldnames + ['Justificación requerida', 'Justificación recibida']
        escritor = csv.DictWriter(fich_escr, fieldnames=campos)
        escritor.writeheader()
        for linea in dict_lector:
            linea['Justificación requerida'] = "Sí" if float(linea['Importe']) > 300 else "No"
            linea['Justificación recibida'] = "No"
            escritor.writerow(linea)


def convert_csv_tsv(fichero_in, fichero_out):
    with open(fichero_in, encoding='utf-8') as fich_lect, \
    open(fichero_out, 'w', encoding='utf-8') as fich_escr:
        dict_lector = csv.DictReader(fich_lect)
        escritor = csv.DictWriter(fich_escr, delimiter='\t', fieldnames=dict_lector.fieldnames)
        escritor.writeheader()
        for linea in dict_lector:
            escritor.writerow(linea)


def excel_file():
    with xlrd.open_workbook('subvenciones.xls') as libro:
        asocs = {}
        for hoja in libro.sheets():
            for i in range(1, hoja.nrows):
                fila = hoja.row(i)
                #print(fila[0].value, fila[1].value, fila[2].value)
                asoc = fila[0].value
                subvencion = fila[2].value
                asocs[asoc] = asocs.get(asoc, 0) + subvencion
        print(asocs)

def json_file():
    with open('subvenciones.json', encoding='utf-8') as fich_lect, \
        open('subvenciones_reformateado.json', 'w', encoding='utf-8') as fich_escr:
        datos = json.load(fich_lect)
        asoc_str = "Asociación"
        act_str = "Actividad Subvencionada"
        imp_str = "Importe en euros"
        lista, list_act = [], []
        asoc_actual, dicc = "", {}
        for elem in datos:
            asoc = elem[asoc_str]
            act = elem[act_str]
            imp = elem[imp_str]
            if asoc_actual != asoc:
                if asoc_actual != "":
                    dicc["Actividades"] = list_act
                    lista.append(dicc)
                list_act = []
                dicc = {"Asociación": asoc}
            list_act.append({act_str: act, imp_str: imp})
            asoc_actual = asoc
        if dicc and list_act:
            dicc["Actividades"] = list_act
            lista.append(dicc)
        json.dump(lista, fich_escr, ensure_ascii=False, indent=4)

def xml_file():
    arbol = ET.parse('subvenciones.xml')
    raiz = arbol.getroot()
    asocs = {}
    for fila in raiz.findall('Row'):
        centro = fila.find('Asociaci_n').text
        subvencion = float(fila.find('Importe').text)
        asocs[centro] = asocs.get(centro, 0) + subvencion
    print(asocs)

def xml_arbol():
    arbol = ET.parse('subvenciones.xml')
    raiz = arbol.getroot()
    asocs = {}
    for fila in raiz.findall('Row'):
        centro = fila.find('Asociaci_n').text
        subvencion = float(fila.find('Importe').text)
        asocs[centro] = asocs.get(centro, 0) + subvencion
    print(asocs)
    
    nuevo = ET.ElementTree()
    raiz_nueva = ET.Element("Raiz")
    nuevo._setroot(raiz_nueva)

    for centro, total in asocs.items():
        elem_actual = ET.SubElement(raiz_nueva, "Asociacion")
        elem_actual.set('nombre', centro)
        actividades = ET.SubElement(elem_actual, "Actividades")
        # Por simplicidad, asociar aquí las actividades si se dispone del listado original
        gas_total = ET.SubElement(elem_actual, "Total")
        gas_total.text = str(total)

    xml_string = ET.tostring(raiz_nueva, encoding='utf-8', method='xml')
    formatted_xml = xml.dom.minidom.parseString(xml_string).toprettyxml(indent="   ")

    with open('subvenciones_reorganizado.xml', 'w', encoding='utf-8') as f:
        f.write(formatted_xml)

if __name__ == "__main__":
    read_csv()
    add_columns()
    convert_csv_tsv('subvenciones.csv', 'subvenciones.tsv')
    excel_file()
    json_file()
    xml_file()
    xml_arbol()
