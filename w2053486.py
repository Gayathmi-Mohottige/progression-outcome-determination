# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solusion.

# Student ID: w2053486
# Student ID (IIT): 20232182

# Student name: Gayathmi Mehansa Mohottige

# Date: 12/12/2023



#initializing variables to track the number of progresses, trailers, retrievers, excludes. 
progress = 0
trailer = 0 
retriever = 0   
exclude = 0     

#Initializing a variable to count the number of total outcomes.
total = 1


#Lists to store input data of the progression outcomes.
progressList = []
trailerList = []
retrieverList = []
excludeList = []


#Function to print the massege "out of range".
def outOfRange():
    print("out of range.")



#deciding whether the user is a student or a staff member.
while True:
        #Get the user input.
        choice = str(input("If you are a student please enter 'a'\nIf you are a staff member please enter 'b'\nEnter your choice :").lower())
        if choice == "a" or choice == "b":
            break
        
        else:
            #Error handling when other than 'a' or 'b' entered. 
            print("ERROR!\nYour choice has to be 'a' or 'b'")
        



#For STUDENTS.

if choice == "a" :
    while True:
         #Getting inputs of pass credit, defer credit, fail credit.
        try:
            pass_credit = int(input("Please enter your credits at pass: "))
            if pass_credit not in range(0,121,20):   #Check if the input is in the correct range.
                outOfRange()   #Print out of range function.   
                continue   

        
            defer_credit = int(input("Please enter your credits at defer: "))
            if defer_credit not in range(0,121,20):  #Check if the input is in the correct range.
                outOfRange()   #Print out of range function.
                continue
        

            fail_credit = int(input("Please enter your credits at fail: "))
            if fail_credit not in range(0,121,20):   #Check if the input is in the correct range.
                outOfRange()   #Print out of range function. 
                continue
        


                    
            if pass_credit + defer_credit + fail_credit != 120:    #Checking the total. 
                print("Total incorrect.")
                continue
                       
                         
                             
        except ValueError :         #Exception handeling for value error.
                print("Integer required")
                continue



#Progression outcome determination.
        if pass_credit == 120:
            print("Progress")
            break

        elif pass_credit == 100:
            print("Progress (module trailer)")
            break

        elif fail_credit < 80 :
            print("Do not progress-module retriever")
            break

        elif fail_credit >= 80 :
            print("Exclude")
            break

                     





#For STAFF MEMBERS.

if choice == "b" :
             while True:
                 #Getting inputs of pass credit, defer credit, fail credit.

                 while True:
                     try:
                         pass_credit = int(input("Please enter your credits at pass: "))
                         if pass_credit not in range(0,121,20):    #Check if the input is in the correct range.
                             outOfRange()    #Print out of range function.     
                             continue   

        
                         defer_credit = int(input("Please enter your credits at defer: "))
                         if defer_credit not in range(0,121,20):   #Check if the input is in the correct range.
                             outOfRange()    #Print out of range function. 
                             continue
        

                         fail_credit = int(input("Please enter your credits at fail: "))
                         if fail_credit not in range(0,121,20):    #Check if the input is in the correct range.
                             outOfRange()    #Print out of range function.
                             continue
        


                    
                         if pass_credit + defer_credit + fail_credit != 120:    #Checking the total. 
                            print("Total incorrect.")
                            continue

                         #If above conditions are met breaking out of the loop. 
                         else:
                             break
                             
                     except ValueError :        #Exception handeling for value error.
                         print("Integer required")


#Progression outcome determination.
                 while True:
                     if pass_credit == 120:
                        print("Progress")
                        data1 = [pass_credit, defer_credit, fail_credit]
                        #Store data in the progressList 
                        progressList.append(data1)    
                        progress += 1      #Increment the progress counter. 
                        break

                     elif pass_credit == 100:
                        print("Progress (module trailer)")
                        data2 = [pass_credit, defer_credit, fail_credit]
                        #Store data in the trailerList.
                        trailerList.append(data2)      
                        trailer += 1       #Increment the progress counter.
                        break

                     elif fail_credit < 80 :
                        print("Do not progress-module retriever")
                        data3 = [pass_credit, defer_credit, fail_credit]
                        #Store data in the retrieverList.
                        retrieverList.append(data3)   
                        retriever += 1     #Increment the progress counter. 
                        break

                     elif fail_credit >= 80 :
                        print("Exclude")
                        data4 = [pass_credit, defer_credit, fail_credit]
                        #Store data in the excludeList.
                        excludeList.append(data4)     
                        exclude += 1       #Increment the progress counter.   
                        break



                 #Prompt to continue or quit.
                 another_set = str(input("Whould you like to enter another data set?\nEnter any key to continue or 'q' to quit and view results: ").lower())


                 #Break the loop if "q" is added. 
                 if another_set == "q":
                     break

                 else :
                    total += 1       #Incrementing the total counter. 
                    continue

             


#Histogram.

if choice =="b" and another_set == "q" :

    #Import the required graphics library. 
    from graphics import *

    def main():
        win = GraphWin("My Histogram", 700,600)  #Create the window.
        win.setBackground (color_rgb(255, 250, 230))#Set the background colour. 

        #Draw the line for the histogram.
        aLine = Line(Point(50,560) , Point(550,560))
        aLine.draw(win)


        #Create the rectangles for the bars.
        bar_1 = Rectangle(Point(120,win.getHeight() - (progress * 45)) , Point(200,560))
        bar_2 = Rectangle(Point(230,win.getHeight() - (trailer * 45)) , Point(310,560))
        bar_3 = Rectangle(Point(340,win.getHeight() - (retriever * 45)) , Point(420,560))
        bar_4 = Rectangle(Point(450,win.getHeight() - (exclude * 45)) , Point(530,560))


        import random

        #list of the colors for the bars.
        colors = ["pink", "plum", "rosybrown", "skyblue" , "lightsalmon", "palegreen" ]


        #Choose random colors from the list and assign them to each bar.
        #Remove them from the initial list to make sure no repitition of colors.
        ranColor1 = random.choice(colors)
        bar_1.setFill(ranColor1)
        colors.remove(ranColor1) 

        ranColor2 = random.choice(colors) 
        bar_2.setFill(ranColor2)
        colors.remove(ranColor2) 
        
        ranColor3 = random.choice(colors) 
        bar_3.setFill(ranColor3)
        colors.remove(ranColor3) 
        
        ranColor4 = random.choice(colors) 
        bar_4.setFill(ranColor4)
        colors.remove(ranColor4)
        
        #Draw the bars.
        if progress > 0 :
            bar_1.draw(win)
        if trailer > 0 :
            bar_2.draw(win)
        if retriever > 0 :
            bar_3.draw(win)
        if exclude > 0 :
            bar_4.draw(win)
     
        

        #Add the lables to each bar.
        #Add the numerical value of each bar.
        text1 = Text(Point(150, 570) , "Progress")
        text1.draw(win)
        num1 = Text(Point(150, win.getHeight() - ((progress * 45) + 16)) , str(progress))
        num1.draw(win)


        text2 = Text(Point(260, 570) , "Trailer")
        text2.draw(win)
        num2 = Text(Point(260, win.getHeight() - ((trailer * 45) + 16)) , str(trailer))
        num2.draw(win) 

        text3 = Text(Point(370, 570) , "Retriever")
        text3.draw(win)
        num3 = Text(Point(370, win.getHeight() - ((retriever * 45) + 16)) , str(retriever))
        num3.draw(win)

        text4 = Text(Point(480, 570) , "Exclude")
        text4.draw(win)
        num4 = Text(Point(480, win.getHeight() - ((exclude * 45) + 16)) , str(exclude))
        num4.draw(win)

        #Display the total number of outcomes.
        totalText = Text(Point(340,34) , str(total)+ " outcomes in total.")
        totalText.draw(win)

        #Display the topic of the histogram.
        topicText = Text(Point(150,10), "Histogram Results.")
        topicText.draw(win)

        #Mouse click to close the window.
        win.getMouse()
        win.close()

    main()


print()


#Part 2 - Lists.
#Printing the lists.

if choice == "b" :
    print("Part 2:")

    #Print the progressList items.
    for i in progressList :
        print(f"Progress - {i[0]}, {i[1]}, {i[2]}")

    #Print the trailerList items.
    for i in trailerList :
        print(f"Progress(module trailer) - {i[0]}, {i[1]}, {i[2]}")

    #Print the retrieverList items.
    for i in retrieverList :
        print(f"Module retriever - {i[0]}, {i[1]}, {i[2]}")

    #print the excludeList items.
    for i in excludeList :
        print(f"Exclude - {i[0]}, {i[1]}, {i[2]}")

print()




#Part 3 - Text File.
#Save inputted progression data to a text file.

if choice == "b" :
    print("Part 3:")


#Open the file for writting.
f = open("test.txt" , "w")

#Write the progressList data to the file.
for i in progressList :
    f.write(f"Progress - {i[0]}, {i[1]}, {i[2]}\n")

#Write the trailerList data to the file.
for i in trailerList :
    f.write(f"Progress(module trailer) - {i[0]}, {i[1]}, {i[2]}\n")

#Write the retrieverList data to the file.
for i in retrieverList :
    f.write(f"Module retriever - {i[0]}, {i[1]}, {i[2]}\n")

#Write the excludeList data to the file.
for i in excludeList :
    f.write(f"Exclude - {i[0]}, {i[1]}, {i[2]}\n")

f.close()



#Open the file for reading.
f = open("test.txt" , "r")

#Read the content of the file and intialize it to a variable.
printCredits = f.read()

f.close()


#Print the content read from the text file.
print(printCredits)





    



        
        

     






    
    
    





        


