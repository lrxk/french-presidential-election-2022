import matplotlib.pyplot as plt
import pandas as pd

labels = ["Arthaud", "Roussel", "Macron", "Lassalle", "Le Pen", "Zemmour",
          "Mélanchon", "Hidalgo", "Jadot", "Pécresse", "Poutou", "Dupont-Aignan"]
labels2ndTour = ["Macron", "Le Pen"]
colorFirstRound = ['#8b0000', '#FF0000', '#add8e6', '#582900', '#00008b', '#000000',
                   '#ff7f00', '#FFC0CB', 'g', '#0000FF', '#D3D3D3', '#ffef00']
color_second_round = ['#add8e6', '#00008b']
def pieChartDepFirstRound(labels, color):
    df_dpt_first_round = pd.read_csv(
        'Data/XLSX/Results/Departement/First_Round/resultats-par-niveau-dpt-t1-france-entiere.csv')
    columns = []
    noms_dpt = df_dpt_first_round["Libellé du département"]
    for i in range(19, len(df_dpt_first_round.columns), 3):
        column = df_dpt_first_round.columns[i]
        columns.append(column)
    df_dpt_first_round=df_dpt_first_round[columns]
    for i in range(len(df_dpt_first_round)):
        #print((df_dpt_first_round.loc[i]))
        plt.pie(df_dpt_first_round.loc[i], labels=labels, colors=color)
        plt.axis('equal')
        plt.tight_layout()
        # if a row contains '/' replace it with '-'
        noms_dpt[i] = str(noms_dpt[i]).replace('/', '-')
        plt.savefig("Data/XLSX/Results/Departement/First_Round/Plot/" +
                    str(noms_dpt[i])+".png")
        plt.close()

def pieChartDepSecondRound(labels, color):
    df_dpt_second_round = pd.read_csv(
        'Data/XLSX/Results/Departement/Second_Round/resultats-par-niveau-dpt-t2-france-entiere.csv')
    columns = []
    noms_dpt = df_dpt_second_round["Libellé du département"]
    for i in range(19, len(df_dpt_second_round.columns), 3):
        column = df_dpt_second_round.columns[i]
        columns.append(column)
    df_dpt_second_round=df_dpt_second_round[columns]
    
    for i in range(len(df_dpt_second_round)):
        plt.pie(df_dpt_second_round.loc[i], labels=labels, colors=color)
        plt.axis('equal')
        plt.tight_layout()
        noms_dpt[i] = str(noms_dpt[i]).replace('/', '-')
        plt.savefig("Data/XLSX/Results/Departement/Second_Round/Plot/" +
                    str(noms_dpt[i])+".png")
        plt.close()

def pieChartRegFirstRound(labels, color):

    df_reg_first_round = pd.read_csv(
        'Data/XLSX/Results/Region/First_Round/resultats-par-niveau-reg-t1-france-entiere.csv')
    columns = []
    noms_reg = df_reg_first_round["Libellé de la région"]
    for i in range(19, len(df_reg_first_round.columns), 3):
        column = df_reg_first_round.columns[i]
        columns.append(column)
    df_reg_first_round=df_reg_first_round[columns]
    for i in range(len(df_reg_first_round)):
        plt.pie(df_reg_first_round.loc[i], labels=labels, colors=color)
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig("Data/XLSX/Results/Region/First_Round/Plot/" +
                    str(noms_reg[i])+".png")
        plt.close()


def pieChartRegSecondRound(labels, color):
    df_reg_second_round = pd.read_csv(
        'Data/XLSX/Results/Region/Second_Round/resultats-par-niveau-reg-t2-france-entiere.xlsx')
    columns = []
    noms_reg = df_reg_second_round["Libellé de la région"]
    for i in range(19, len(df_reg_second_round.columns), 3):
        column = df_reg_second_round.columns[i]
        columns.append(column)
    df_reg_second_round=df_reg_second_round[columns]
    for i in range(len(df_reg_second_round)):
        plt.pie(df_reg_second_round.loc[i], labels=labels, colors=color)
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig("Data/XLSX/Results/Region/Second_Round/Plot/" +
                    str(noms_reg[i])+".png")
        plt.close()
pieChartDepFirstRound(labels,colorFirstRound)
pieChartDepSecondRound(labels2ndTour,color_second_round)
pieChartRegFirstRound(labels,colorFirstRound)
pieChartRegSecondRound(labels2ndTour,color_second_round)
