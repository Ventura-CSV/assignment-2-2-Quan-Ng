def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input('Enter Celsius: '))
    farenheit = (1.8 * celsius) + 32
    
    print (f'Farenheit \t {farenheit: .2f}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, farenheit


if __name__ == '__main__':
    main()
