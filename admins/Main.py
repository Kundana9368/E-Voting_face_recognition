from DBConnection import DBConnection
from Predict_KNN import predict,show_prediction_labels_on_image,train
import sys
import os

def classify_face(img):
        try:
        
            # print("Training KNN classifier...")
            classifier = train("./faces", model_save_path="trained_knn_model.clf", n_neighbors=1)
            # print("Training complete!")

            # Using the trained classifier, make predictions for unknown images
            for image_file in os.listdir("./test"):
                full_file_path = os.path.join(img, image_file)

            # print("Looking for faces in {}".format(image_file))

            # Find all people in the image using a trained classifier model
            # Note: You can pass in either a classifier file name or a classifier model instance
                predictions = predict(full_file_path, model_path="trained_knn_model.clf")

                print("The photo name is",predictions[0][0])

                show_prediction_labels_on_image(os.path.join("./test", image_file), predictions)

            
            print("finish")
            



        except Exception as e:
                    print(e.args[0])
                    tb = sys.exc_info()[2]
                    print(tb.tb_lineno)
                    print(e)
