import os
import pandas as pd



class Refiner:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_xlsx_file(self):
        all_files = os.listdir(self.filepath)
        xlsx_file = []
        for file in all_files:
            if file.endswith('.xlsx'):
                # file with full path
                xlsx_file.append(os.path.join(self.filepath, file))
        return xlsx_file
    def refine_result(self):
        first_round_str = [os.path.join(self.filepath, "resultats-par-dpt-t1-france-entiere.xlsx"),
                           os.path.join(self.filepath, "resultats-par-reg-t1-france-entiere.xlsx")]
        for file in self.get_xlsx_file():
            df = pd.read_excel(file)
            if file == first_round_str[0] or file == first_round_str[1]:
                self.individual_refiner_first_round(df).to_csv(
                    file[0:len(file)-5]+".csv", index=False)
            else:
                self.individual_refiner_second_round(df).to_csv(
                    file[0:len(file)-5]+".csv", index=False)
        pass
    def get_candidates_order(self, df: pd.DataFrame,round):
        """ Get the order of the candidates """
        candidates_order = []
        # return the first line of the dataframe
        df.loc[0]
        if round == "first":
            for i in range(1, 13):
                candidates_order.append(df.columns[i])
        else:
            for i in range(1, 3):
                candidates_order.append(df.columns[i])
        return candidates_order

    def str_candidats(self, df: pd.DataFrame, round):
        """ Create column names """
        df.columns[0:23]
        str_candidat = "_candidat_"
        str_candidats = []
        # get the order of the candidates depending on the round
        candidates_order = self.get_candidates_order(df,round)
        for i in range(len(candidates_order)):
            str_candidats.append(str_candidat+candidates_order[i])
        return str_candidats

        

    def columns_to_repeat(self, df: pd.DataFrame):
        columns_to_repeat = []
        for i in range(17, 23):
            columns_to_repeat.append(df.columns[i])
        return columns_to_repeat

    def new_columns(self, df, round):

        str_candidats = self.str_candidats(df, round)
        columns_to_repeat = self.columns_to_repeat(df)
        new_columns = []
        for i in range(len(str_candidats)):
            for column in columns_to_repeat:
                new_columns.append(column+str_candidats[i])
        new_columns = self.columns_not_to_replace(df)+new_columns
        return new_columns

    def columns_not_to_replace(self, df):
        columns_not_to_replace = []
        for i in range(0, 17):
            columns_not_to_replace.append(df.columns[i])
        return columns_not_to_replace
    # associate the actual column name to the future one
    def rename_column_dict(self, df, round):
        new_columns = self.new_columns(df, round)
        rename_column_dict = {}
        for i in range(len(new_columns)):
            rename_column_dict.update({df.columns[i]: new_columns[i]})
        return rename_column_dict

    def individual_refiner_first_round(self, df: pd.DataFrame):
        df = df.rename(columns=self.rename_column_dict(df, "first"))
        return df

    def individual_refiner_second_round(self, df: pd.DataFrame):
        df = df.rename(columns=self.rename_column_dict(df, "second"))
        return df

    