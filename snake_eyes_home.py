# importing Flask and other modules
from flask import Flask, request, render_template
from classifier import classify
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       length = request.form.get("length")
       thickness = request.form.get("thickness")
       head_shape = request.form.get("head_shape")
       head_size = request.form.get("head_size")
       colour = request.form.get("colour")
       pattern = request.form.get("pattern")
       movements = request.form.get("movements")
       spotted_area = request.form.get("spotted_area")
       spotted_time = request.form.get("spotted_time")

       length = str(length).strip()
       thickness = str(thickness).strip()
       head_shape = str(head_shape).strip()
       head_size = str(head_size).strip()
       pattern = str(pattern).strip()
       movements = str(movements).strip()
       spotted_area = str(spotted_area).strip()
       spotted_time = str(spotted_time).strip()
       colour = str(colour).strip()

       if(spotted_time == 'Day' ):
         spotted_time = 'no'
       if(spotted_time == 'Night' ):
         spotted_time = 'Yes'
       input_list = [thickness,head_shape,head_size,colour,pattern,spotted_time,movements,spotted_area,float(length)]
#       return "Input IS "+ str(length) + str(thickness) + str(head_shape) + str(head_size) + str(colour) + str(pattern) + str(movements)  + str(spotted_area) + str(spotted_time)
       return render_template(classify.predict_species(input_list)+".html")


    return render_template("home_snake_eyes.html")

    #
    # test_columns = ['Thickness', 'Head shape', 'Head size', 'Colour', 'Pattern',
    #    'Nocturnal', 'Agility', 'Habitat', 'Length_normalized']


if __name__=='__main__':
   app.run()
