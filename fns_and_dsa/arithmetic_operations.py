def perform_operation(num1, num2, operation):
    
    #match operation:
        #case "add" :
         #   return num1 + num2
        #case "subtract" :
         #   return num1 - num2
        #case "multiply" :
         #   return num1 * num2
        #case "divide":
         #   if num2 == 0 :
          #      print("Cannot divide by 0")
           # else:
            #    return num1 / num2
            
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2==0:
            print("Cannot divide by 0")
        else:
            return num1 / num2