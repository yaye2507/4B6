import time

ma_variable_globale = "mglobale"

def my_arg(ma_variable_argument):

    ma_variable_locale = "mlocale"
    
    for var in [ma_variable_globale, ma_variable_argument, ma_variable_locale]:
        print(var)
        time.sleep(1)  

my_arg("ma_variable_argument")
