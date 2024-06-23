from os import stat
from django.http import response
from django.shortcuts import render, redirect
import sys
import cv2
import mysql.connector

from manage import main
from .face_rec import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            print("Hello world", username, password)
            # print("retive from database",Adminlogin.objects.get(username))
            # enter=Adminlogin.objects.get(username=username,password=password)
            if (username == "admin" and password == "admin"):
                request.session["name"] = username

                return redirect('AdminHome')
            elif (username == "server" and password == "server"):
                request.session["name"] = username
                return redirect("ServerHome")

            elif(username=="sai" and password=="sai"):
                 request.session["name"] = username
                 return redirect("ServerHome")






        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    return render(request, 'login.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def AdminHome(request):
    return render(request, 'AdminHome.html')


def VoteCandidate(request):
    if request.method == "POST":

        name = request.POST.get('photo')
        if (name == "TakePhoto"):

            cam = cv2.VideoCapture(0)

            cv2.namedWindow("Python Webcam ScreenShot App")

            img_counter = 0

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)

                k = cv2.waitKey(1)

                if (k % 256 == 27):

                    print("esc hit")
                    break

                elif (k % 256 == 32):
                    # img_name="opencv_frame_{}.png".format(img_counter)
                    img_name = "bruno.png"

                    img_counter = img_counter + 1

                    cv2.imwrite(img_name, frame)
                    cv2.imwrite("test/bruno.png", frame)

                    print("screenshot taken")

            cam.release()

            cv2.destroyAllWindows()
        elif (name == "Submit Vote"):

            pname = request.POST.get('c1')
            uname = request.POST.get("username")

            print(pname)

            print(uname)

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="evoting")

            mycursor = mydb.cursor()

            sql = "INSERT INTO voting (uname, pname) VALUES (%s, %s)"
            val = (uname, pname)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

            return redirect('VoterSubmit')

        else:
            print("Take vote")

            photoname = classify_face("bruno.png")

            print(photoname)

            info = []
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="evoting")

            mycursor = mydb.cursor()

            sql = "SELECT * FROM voting"

            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            info.append(photoname)

            status = 0
            flag = 0
            for x in myresult:
                print(x)
                print("The photo name is ", photoname)
                if (photoname[0] == "Unknown"):
                    flag = 1
                print("The username is ", x[0])

                if (photoname[0] == x[0]):
                    status = 1
                    break

            print("The status is ", status)

            if (flag == 1):
                return render(request, 'unknown.html')

            if (status == 1):
                return render(request, 'VotersInformation1.html', {'name': photoname[0], 'status': status})
            else:
                return render(request, 'VotersInformation.html', {'name': photoname[0], 'status': status})

    return render(request, 'VoteCandidate.html')


def VoterSubmit(request):
    return render(request, 'VoterSubmit.html')


def ServerHome(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="evoting")

    mycursor = mydb.cursor()
    #mycursor1 = mydb.cursor()

    sql = "SELECT count(*) FROM voting where pname='president1'"
    #sql1 = "SELECT count(*),count(*) FROM voting where pname='president2' and pname='president1'"

    mycursor.execute(sql)
    #mycursor1.execute(sql1)
    myresult = mycursor.fetchall()
    #myresult1 = mycursor1.fetchall()
    for x in myresult:
        print(x)
    a1=x[0]

    mydb1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="evoting")

    mycursor1 = mydb.cursor()
    # mycursor1 = mydb.cursor()

    sql1 = "SELECT count(*) FROM voting where pname='president2'"
    # sql1 = "SELECT count(*),count(*) FROM voting where pname='president2' and pname='president1'"

    mycursor1.execute(sql1)
    # mycursor1.execute(sql1)
    myresult1 = mycursor1.fetchall()
    # myresult1 = mycursor1.fetchall()
    for y in myresult1:
        print(y)
    a2=y[0]
    if(a1>a2):
        print("President 1 wins")
    else:
        print("President 2 wins")





    return render(request, 'majority.html', {'name': x,'name1':y})
