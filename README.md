# potato-disease-detection-DNN
### download the repo and have tensorflow serving container downloaded from docker
1. running tensorflow serving container container
  docker run --name tensflow-serving-server \
  -p 8501:8501 \
  -v /deep-neural-network-project:/potato_disease \
  tensorflow/serving \
  --rest_api_port=8501 \
  --model_config_file=/potato_disease/potato_tf_serving_config.a
   
  note: deep-neural-network-project is this project location 

  3. start fastapi server by running python file
       deep-neural-network-project/api/main-tf-serving.py

  4. cd frontend folder
       a. npm install --from-lock-json
       b. npm start //in the frontend directory to start the frontend-server
       c. drag and drop images to see the result
