import plotly.express as px
conf_records = []

def get_confidence():
    # Prompt user for input
    number = input("How confident do you feel right now on learning the content above? \n0 - Least confident; 100 - Most confident \nPlease enter an integer between 0 and 100: ")
    # Validate input
    while True:
        number = int(number)
        if 0 <= number <= 100:
            break
        number = input("Invalid input. Please try again. \nPlease enter an integer between 0 and 100: ")
    print(f"The integer you entered is: {number}")
    # Add the number to the list
    conf_records.append(number)
    
def plot_confidence():
    fig = px.line(y=conf_records, range_y=[0, 100])
    fig.update_layout(
        xaxis_title="Your entries for this session",
        yaxis_title="Your learning confidence input",
        title="Trend of your learning confidence for this session",title_x=0.5)
    fig.show()