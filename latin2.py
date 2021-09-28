def detect(text):
        if "о'" and "г'" in text:
            answer1=text.replace("г'","ғ")
            answer=answer1.replace("о'","ў")  
        elif "г'" in text:
            answer=text.replace("г'","ғ")
        elif "о'" in text:
            answer=text.replace("о'","ў")
        elif "О'" and "Г'" in text:
            answer1=text.replace("Г'","Ғ")
            answer=answer1.replace("О'","Ў")  
        elif "Г'" in text:
            answer=text.replace("Г'","Ғ")
        elif "О'" in text:
            answer=text.replace("О'","Ў")
        elif "О'" and "г'" in text:
            answer1=text.replace("г'","ғ") 
            answer=answer1.replace("О'","Ў")
        elif "Г'" and "о'" in text:
            answer1=text.replace("о'","ў") 
            answer=answer1.replace("Г'","Ғ")  
        else:
            answer=text
        return answer