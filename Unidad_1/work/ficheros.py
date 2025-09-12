import csv
import xlrd



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

if __name__ == "__main__":
    #read_csv()
    #add_columns()
    #convert_csv_tsv('subvenciones.csv', 'subvenciones.tsv')
    excel_file()
