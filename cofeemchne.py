MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 300,
    "coffee": 100,
}



rho=True
machine_money=0

def dollar_count():
    print("Please insert coins")
    dollar_value=int(input("How many quaters?: "))*25
    dollar_value+=int(input("How many dimes?: "))*10
    dollar_value+=int(input("How many nickles?: "))*5
    dollar_value+=int(input("How many pennies?: "))
    # quaters,dimes,nickles,pennies=10*25,1*10,1*5,10
    # dollar_value=pennies+nickles+dimes+quaters
    dollar=dollar_value/100 
    print(f"you inserted {dollar} dollars")
    return dollar


def check_resources(choosen): 
    drink=MENU[choosen]["ingredients"]
    for item in drink:
        if drink[item]>=resources[item]:  
            print("no sufficient resouces in machine,please give us some time") 
            return False
    return True

def changing_main_resources(input_option): 
    input_drink=MENU[input_option]["ingredients"]
    for value in input_drink:
        resources[value]-=input_drink[value]
    return resources    
      
def checking_money(dollars,coffee_cost) :
    if dollars<coffee_cost:
        print(f"please add sufficient money, here is your refund amount{dollars}")
        return False
    else:    
        global machine_money
        machine_money += coffee_cost
        change=dollars-coffee_cost
        print(f"here is your change amount : {change:.2f}")
        print(f"Enjoy your {input_option}")
        return True
# start programṇ
      
while rho:
    
    input_option=input("What would you like to have \(\('cappuccino'\)\/, \('latte'\)\/, \('espresso'\)\/\) : ")
    
    if input_option=="off":
        print("machine is switching off")
        rho=False
        
    elif input_option=="report":   
        print(f"{resources},Machine_Money={machine_money}") 
        
    else:         
            if  check_resources(input_option):
                resources=changing_main_resources(input_option) 
                dollars=dollar_count() 
                coffee_cost=MENU[input_option]["cost"]
                if dollars<coffee_cost:
                     print(f"please add sufficient money, here is your refund amount{dollars}")
                else:    
                    machine_money += coffee_cost
                    change=dollars-coffee_cost
                    print(f"here is your change amount : {change:.2f}")
                    print(f"Enjoy your {input_option}")
            else:
                rho=False    
                
            
       
 