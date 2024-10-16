import pandas as pd


def calcularMediaTemperatura(path: str) -> None:
    dicMediciones: dict = {}
    dtf: pd.DataFrame = pd.read_excel(path)
    for index, row in dtf.iterrows():
        mes: str = row['Fecha'].month
        if mes in dicMediciones:
            dicMediciones[mes].append(row['Medición'])
        else:
            dicMediciones[mes] = [row['Medición']]
    for key in dicMediciones:
        print(f"En el fichero {path} La media del mes {key} es: {sum(dicMediciones[key])/len(dicMediciones[key])}")




def main() -> None:
    calcularMediaTemperatura('Ej_Limp.xlsx')
    calcularMediaTemperatura('Ej_Limp_Actualizado.xlsx')

if __name__ == "__main__":
    main()