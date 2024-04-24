def number_to_month(month):
    
    mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

    if (month>=13) or (month==0):
        
        return ("error")
        
    else:
        
        return mes[month-1]
       
print(number_to_month(5))


