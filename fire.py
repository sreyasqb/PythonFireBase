
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
# rest_text='''Rest period is to relax the muscles to which you have given workouts, Stepping/squats would have stiffened the muscles in your thigh muscles and other parts of your legs , so shake your thigh muscles, other parts of legs and loosen it up by slow walking or jogging'''
id="L1_C2"
data={
    'title':'''Flexibility Exercises
''',
    'description':'''Do stretching movements for your muscles like hamstring and greater rhomboid by doing the toe touching flexibility exercise and do lounging exercise to stretch your adductor and gastrocnemius muscles.  Unlike doing these exercises during the warming-up time, during warming-down these exercises should be done in much slower phase
    ''',
    'id':id,
    'setCount':1,
    'time':"05:00",
    'calorieValue':5,
    'isRest':False,
    'youtubeUrl':"Not Available",
    'imageUrl':"",
#     'musclesStrengthened':'''
#     Upper Body Workout
# It strengthen the Triceps – back of the Biceps muscles and also strengthens wrist and fore arm
#  '''


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
# db.collection('ExerciseData').document(id).set(data)

jumpingJack ="https://assets8.lottiefiles.com/packages/lf20_btqxjpsz.json"
pushups = "https://assets4.lottiefiles.com/packages/lf20_QegQCG.json"
squats="https://s36370.pcdn.co/wp-content/uploads/2017/02/Wall-Squats.jpg"
mount="https://media1.popsugar-assets.com/files/thumbor/Iu8waoj6rmL6c7B8gZUdS1ZIa3I/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/06/08/791/n/1922729/c4943793a2ba2dd5_SlowerClimbers.gif"
planks="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhWo1HIry93gjaAKf696iaALYsBcfzgL9OCA&usqp=CAU"
# stepping="https://www.healthier.qld.gov.au/wp-content/uploads/2015/07/21_M_WIP02.gif"
stepping="https://3i133rqau023qjc1k3txdvr1-wpengine.netdna-ssl.com/wp-content/uploads/2014/08/Up-Up-Down-Down_Exercise.jpg"
skipping="https://assets7.lottiefiles.com/packages/lf20_5ucyqblz.json"
dips="https://media4.giphy.com/media/4zIMiq61O8M2ZBxfRv/giphy.gif"
crunches="https://assets8.lottiefiles.com/packages/lf20_Ajcy3F.json"
calf="https://thumbs.gfycat.com/DefinitiveEnlightenedAmurminnow-size_restricted.gif"
rest="https://assets2.lottiefiles.com/private_files/lf30_3k3mez5t.json"
jjf="https://www.google.com/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/2/23/Skierjacks.gif&imgrefurl=https://commons.wikimedia.org/wiki/File:Skierjacks.gif&tbnid=1pyefh-YG4xN9M&vet=1&docid=5If39-A8OSHLbM&w=640&h=480&itg=1&source=sh/x/im"


#level3
dips_l3="https://flabfix.com/wp-content/uploads/2019/05/Triceps-Bench-Dips-with-Straight-Legs.gif"

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

#warmup links
run=""
highKnee="https://www.icegif.com/wp-content/uploads/high-knees-icegif.gif"
breathing=""
forwardTilt="https://thumbs.gfycat.com/BlackYearlyJumpingbean-size_restricted.gif"
sidewardTilt="https://im.idiva.com/content/2020/Oct/12-1_5f9c0bcdb8b93.gif"
sidewardTurn="https://www.verywellhealth.com/thmb/taKjtLDviSbEU0yQnLvE2GGry2M=/1500x1000/filters:no_upscale():max_bytes(150000):strip_icc()/Verywell-23-2696365-SideToSide01-1908-59933a3fd088c00013cd036f.gif"
chinRoll=""
headRotation="https://www.talkingtrendo.com/wp-content/uploads/2020/03/785914_887fe82452cd4df2b47fd58378a90bc5.gif"
armSwinging=""
armRotation="https://177d01fbswx3jjl1t20gdr8j-wpengine.netdna-ssl.com/wp-content/uploads/2019/09/ArmCircles.gif"
trunkTwist=""
toeTouch="https://photos.demandstudios.com/getty/article/178/215/78629463.jpg"
sideStrech="https://i.pinimg.com/originals/2f/99/0c/2f990cb1c506615126817ff60fb4601e.gif"
oppToeTouch="https://i.pinimg.com/originals/7b/87/b8/7b87b85072778d543f2ebe3cd57e764c.png"
forwardBending=""
lunging="https://c.tenor.com/PF7Q7Qu1wJEAAAAM/lunges.gif"
ankleRotation="https://www.spotebi.com/wp-content/uploads/2015/03/ankle-circles-exercise-illustration.jpg"
forearmFlexor="https://images-prod.healthline.com/hlcmsresource/images/topic_centers/Fitness-Exercise/400x400_5_Good_Yoga_Stretches_For_Your_Arms_Fingers_Up_and_Down_Stretch.gif"
forearmExtonser="https://thumbs.gfycat.com/ColorfulViciousJellyfish-max-1mb.gif"
tricepStrech="https://www.vissco.com/wp-content/uploads/animation/sub/triceps-stretch.gif"

stuff={'imageUrl':tricepStrech}
db.collection('ExerciseData').document('L1_W18c').update(stuff)

#lists
jjL=["L1_1","L2_1","L3_1",'L4_1','L4_1_F']
jjfL=["L2_2",'L3_2','L4_2','L4_2_F']
steppingL=["L1_2","L2_3",'L4_3']
pushupL=["L1_3","L2_4",'L3_4_F']
squatsL=["L1_4","L2_6",'l4_7']
planksL=["L1_5","L2_7",'L3_8','L3_8_F','L4_8']
dipsL=["L1_6",'L3_9']
calfL=["L1_7","L2_9","L3_10","L3_10_F",]
crunchesL=["L2_10",'L3_11','L3_11_F','L4_11']
mountL=["L2_5",'L4_6']
skippingL=["L3_5",'L4_5']

#Warmup List
warmupL=["L1_W1","L1_W2","L1_W3","L1_W4","L1_W5","L1_W6","L1_W7","L1_W8","L1_W9","L1_W10","L1_W11","L1_W12",'l1_W13','l1_W14','l1_W15','L1_W16','L1_W17','L1_W18a','L1_W18b','L1_W18c']
cdL=["L1_C1","L1_C2"]

#updating the warmup list
# levD=db.collection('WomenLevelData').document('Level 1').get().to_dict()
# existing_list=levD['exerciseIds']
# new_list=warmupL+existing_list+cdL
# # print(new_list)
# excData={'exerciseIds':new_list}
# db.collection('WomenLevelData').document('Level 4').update(excData)


# stuff={'description':rest_text}
# stuff={'imageUrl':stepping}
# for i in steppingL:
#     db.collection('ExerciseData').document(i).update(stuff)




# stuff={'imageUrl':dips}
# db.collection('ExerciseData').document('L1_R2').update(stuff)
# db.collection('ExerciseData').document(id).set(data)
# db.collection('ExerciseData').document(id).set(dataR)
# string='''It strengthens the core muscles
# '''
# menD=db.collection('MenLevelData').document('Level 4').get().to_dict()
# db.collection('WomenLevelData').document('Level 4').set(menD)
# db.collection('ExerciseData').document('L1_3').update(stuff)

# d=db.collection('ExerciseData').document('L3_11').get().to_dict()
# d['setCount']=12
# d['id']="L4_11"
# d['time']="00:30"
# db.collection('ExerciseData').document("L4_11").set(d)
