# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2051998
# Date: 14.12.2023

from graphics import *

p_count=0              #progress count
m_trailer_count=0      #Prograss(module trailer) count
m_retriver_count=0     #Module retriver count
e_count=0              #Exclude count


#list
p_list =[]
m_trailer_list=[]
m_retriver_list =[]
e_list=[]

text_output=open("Text_input.txt","w")   #here i open a file to store data in a file 

#create histogram according to the user's input data
def histogram():

     win=GraphWin("Histogram",750,600)                     #creating window for the histogram
     title=Text(Point(150,50),"Histogram result")          #title for the created window
     title.setSize(20)                                     #set the title size for the window
     title.setStyle("bold")                                 #seting the font style
     title.draw(win)                                      
    
     total=p_count+m_trailer_count+m_retriver_count+e_count           #Total count of all outcome
     reasults=["Progress","Trailer", "Retriver", "Exclude"]             #These are used in x axies of graph for the identification of rectangle(bar)
     colors=[color_rgb(174,248,161), color_rgb(160,198,137), color_rgb(167,188,119), color_rgb(210,182,181)]             #these are the colors that used for reactangr/bar


     #line
     xaxis=Line(Point(50,500),Point(650,500))         #this is starting and end point of x axies of graph
     xaxis.draw(win)

     #Rectangle
     rec_width=100                  #this  indicates width of recatngle
     rec_space=20                   #this indicates the space between two recatngle/bar
     
     x=100

     max_height=400                                                   #here i assign a maximum  height for the recatngle/bar
     output=p_count,m_trailer_count,m_retriver_count,e_count          #list that show the counts of result
     max_count=max(output)                                            #this show the maximum count of result that given above

     for i, value in enumerate(output):
         rec_height=(value/ max_count)* max_height           #formula to find the height of recatngle,from this we can calculate the rectangle based on the values ana maximum count

        #these are the points that indicates the locatoin of the recatngle
         x1=100+i*(rec_width+rec_space)
         y1=500-rec_height
         x2=x1+rec_width
         y2=500

         #create and drawing the recatngle 
         rectangle = Rectangle(Point(x1, y1), Point(x2, y2))         #points of the rectangle in the graph
         rectangle.setFill(colors[i])                                #colors that assined to the each of the rectangle
         rectangle.draw(win)

         #To disply the count of the result in the top of the rectangle
         result_count = Text(Point((x1 + x2) / 2, y1 - 10), f"{value}")
         result_count.setStyle("bold")
         result_count.setTextColor("grey")
         result_count.draw(win)

         #This shows the result at the bottom of the
         result = Text(Point((x1 + x2) / 2, y2 + 10), f"{reasults[i]}")
         result.setStyle("bold")
         result.setTextColor("grey")
         result.draw(win)

    #this shows final and total outcomes of the user input
     message = Text(Point(200,550), str(total) + " " + "Outcomes in Total")
     message.setSize(20)
     message.setStyle("bold")
     message.draw(win)
     
     try:
        win.getMouse()
        win.close()
     except GraphicsError:
        pass
#this user defined functoin for validation of the input  
def credit_input(message):    
    while True:
        try:
            credit = int(input(message))
            if  credit<0 or credit>120 or credit % 20 != 0:       #this is the condition for the validation for all credit inputs
                print('Out of range')   
                continue
        except ValueError:
             print("Integer requied") 
             continue
        break
    return credit

#user define function for      
def final_outcome(pass_credits,defer_credits,fail_credits):
    global p_count,m_trailer_count,m_retriver_count,e_count,text_output    #Here is the global keyword to indicate that we are referring to the global variable
    if pass_credits + defer_credits +fail_credits !=120:
        return("Total incorrct, Total should be equal to 120")             
    if pass_credits==120:                              #this is a condition to get reult:progress                  
        p_count+=1                                     #here i adding progress outcome to get total outcome
        p_list.append([f"{pass_credits},{defer_credits},{fail_credits}"])               #here i get data to make a list(part 2)
        text_output.write('progress-' + str(pass_credits) + "," + str(defer_credits) + "," + str(fail_credits)+'\n')           #here i get data to make a file(part 3)
        return("progression outcome:Progress")
      
    elif pass_credits==100:                              #this is a condition to get reult:module trailer
        m_trailer_count+=1                               #here i adding module trailer outcome to get total outcome
        m_trailer_list.append([f"{pass_credits},{defer_credits},{fail_credits}"])                       #here i get data to make a list(part 2)       
        text_output.write('Progress(module trailer)-'+ str(pass_credits) + "," + str(defer_credits) + "," + str(fail_credits)+'\n')      #here i get data to make a file(part 3)        
        return("progression outcome:Progress(module trailer)")
    
    elif 60>=fail_credits>=0:                            #this is a condition to get reult:module retriver
        m_retriver_count+=1                              #here i adding module retriver outcome to get total outcome
        m_retriver_list.append([f"{pass_credits},{defer_credits},{fail_credits}"])                      #here i get data to make a list(part 2)   
        text_output.write('progressoin outcome:Module retriver-' + str(pass_credits) + "," +str(defer_credits)+","+str(fail_credits)+'\n')               #here i get data to make a file(part 3) 
        return("progression outcome:Module retriver")
    
    elif  0 <= pass_credits <= 40 and 0 <= defer_credits <= 40 and 80 <= fail_credits <= 120:        #this is a condition to get reult:exclude
        e_count+=1                                                                                   #here i adding exclude outcome to get total outcome
        e_list.append([f"{pass_credits},{defer_credits},{fail_credits}"])                            #here i get data to make a list(part 2)   
        text_output.write('Exclude-'+str(pass_credits)+","+str(defer_credits)+","+str(fail_credits)+'\n')        #here i get data to make a file(part 3) 
        return("progression outcome:Exclude")
    
def input_marks():
    pass_credits=credit_input("Enter the number of credits at pass:")       #ask to enter the pass credits from the user
    defer_credits=credit_input("Enter the number of credits at defer:")     #ask to enter the defer credits from the user
    fail_credits=credit_input("Enter the number of credits at fail: ")      #ask to enter the fail credits from the user
    outcome=final_outcome(pass_credits,defer_credits,fail_credits)
    print(outcome)

#list printing   
def printing_list(printing_message,lists):
    for item in range(len(lists)):
        print(printing_message,"-",lists [item])

#here this user define function used for move into part 2 and part 3
def choices():
    choice = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    if choice not in ["q", "y"]:
        print("Invalid input")
        return choices()
    elif choice == "q":
        # Assuming text_output is defined somewhere before this point
        text_output.close()
        print("\nPart 2")
        printing_list("Progress", p_list)
        printing_list("Progress(module trailer)", m_trailer_list)
        printing_list("Progress(module retrivers)", m_retriver_list)
        printing_list("Excluded", e_list)
        print("\nPart 3")

        with open("Text_input.txt", "r") as file:
            print(file.read())  # Using  statement for file handling

        histogram()  # Calling histogram when quitting
        return True  # Returning True to break the loop

#this is for a confirmation whether user is staff or student
while True:
    ask = input("\nAre you Staff or Student?\nIf you are a Staff enter 'staff' or Student enter 'student': ").lower()

    if ask == "student":
        input_marks()
        break
    elif ask == "staff":
        staff_identification=input("Enter your staff id (Format: w123456) :  ")         #here i using this for a confirmation, reason is only staff can access this facility 
        while True:
            input_marks()      #here  calling user define function for acces the credits  
            if choices():      
                break
        break
    else:
        print("Wrong type entered.")
 




                
                
                

              






