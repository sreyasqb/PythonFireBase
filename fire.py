
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

id="L3_9"
data={
    'title':'''Dips

''',
    'description':'''Take position in front of a step, step shall be with a minimal height of 12 to 18 inches, shall use door step/wooden planks/chair etc., for this purpose, place both the hands on the edge of the step with a couple of inches wider than your shoulder width, with your hip close to the step stretch your legs straight in the supine position, your full body weight will be on your hands, now slowly flex your elbow for few inches so that you take your body downward, only partial flexing of elbow is advised, then move back to the original position, it should be in the DOWN-UP-DOWN-UP movement pattern.  Phasing up should be moderate.  
     ''',
    'id':id,
    'setCount':8,
    'time':"00:25",
    'calorieValue':5,
    'isRest':False,
    'musclesStrengthened':'''
    Upper Body Workout
It strengthen the Triceps – back of the Biceps muscles and also strengthens wrist and fore arm
 ''',
    'youtubeUrl':"Not Available"

}
dataR={
    'title':'Rest',
    'description':'''Rest period is to relax the muscles to which you have given workouts; Skipping would have stiffened the muscles in your legs so shake your thigh muscles and calf muscles and loosen it up by slow walking or jogging, wrist joint and whole of your hands shall also be concentrated in relaxing.  Have deep breathes and breathe out slowly.
    ''',
    'id':id,
    'setCount':1,
    'time':"00:45",
    'calorieValue':5,
    'isRest':True
}
jumpingJack ="https://assets8.lottiefiles.com/packages/lf20_btqxjpsz.json"
pushups = "https://assets4.lottiefiles.com/packages/lf20_QegQCG.json"
squats="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmQzkia_TcAu_FB_M5SJ0VmlT75sb1Tswi9w&usqp=CAU"
mount="https://media1.popsugar-assets.com/files/thumbor/Iu8waoj6rmL6c7B8gZUdS1ZIa3I/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/06/08/791/n/1922729/c4943793a2ba2dd5_SlowerClimbers.gif"
planks="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhWo1HIry93gjaAKf696iaALYsBcfzgL9OCA&usqp=CAU"
stepping="https://www.healthier.qld.gov.au/wp-content/uploads/2015/07/21_M_WIP02.gif"
skipping="https://assets7.lottiefiles.com/packages/lf20_5ucyqblz.json"
dips="https://assets3.lottiefiles.com/packages/lf20_VMnqvY.json"
crunches="https://assets8.lottiefiles.com/packages/lf20_Ajcy3F.json"
calf="https://thumbs.gfycat.com/DefinitiveEnlightenedAmurminnow-size_restricted.gif"
rest="https://assets2.lottiefiles.com/private_files/lf30_3k3mez5t.json"

#yt links
jjyt="https://www.youtube.com/watch?v=1b98WrRrmUs"
pushyt="https://www.youtube.com/watch?v=bt5b9x9N0KU"
squatsyt="https://www.youtube.com/watch?v=YaXPRqUwItQ"
mountyt="https://www.youtube.com/watch?v=nmwgirgXLYM"
planksyt="https://www.youtube.com/watch?v=kL_NJAkCQBg"
steppingyt="https://www.youtube.com/watch?v=WCFCdxzFBa4"
skippingyt="https://www.youtube.com/watch?v=u3zgHI8QnqE"
dipsyt="https://www.youtube.com/watch?v=2z8JmcrW-As"
crunchesyt="https://www.youtube.com/watch?v=Xyd_fa5zoEU"
calfyt="https://www.youtube.com/watch?v=-M4-G8p8fmc"
jjfyt="https://www.youtube.com/watch?v=roHYKy3YKJI"

stuff={'youtubeUrl':planksyt}
db.collection('ExerciseData').document('L4_8').update(stuff)
# db.collection('ExerciseData').document(id).set(data)
# db.collection('ExerciseData').document(id).set(dataR)
# string='''It strengthens the core muscles
# '''
# menD=db.collection('MenLevelData').document('Level 4').get().to_dict()
# db.collection('WomenLevelData').document('Level 4').set(menD)
db.collection('ExerciseData').document('L1_3').update(stuff)

# d=db.collection('ExerciseData').document('L3_11').get().to_dict()
# d['setCount']=12
# d['id']="L4_11"
# d['time']="00:30"
# db.collection('ExerciseData').document("L4_11").set(d)