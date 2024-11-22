🥔🌱 Potato Disease Plant Detection 🌟
Welcome to the Potato Disease Plant Detection project! 🚀 This repository is your one-stop solution for detecting diseases in potato plants using the power of Deep Neural Networks (DNN), TensorFlow Keras, and TensorFlow Serving – all wrapped in a seamless Dockerized workflow. 🐳✨

🌟 What’s Inside?
This project aims to leverage cutting-edge technologies to assist farmers and agronomists in identifying diseases in potato plants efficiently. Here’s a quick peek at what makes this repo awesome:

🤖 Deep Neural Network Model: A robust model trained using TensorFlow Keras, optimized for accuracy.
📦 Docker Integration: A fully containerized application for smooth deployment and scalability.
⚡ TensorFlow Serving: Real-time model serving for ultra-fast predictions.
🖼️ Image Processing: Upload a potato leaf image to get instant disease detection results.
🌐 Scalable Deployment: Deploy anywhere – your local machine or the cloud.
🚀 How It Works?
Train the Model: Train your own model or use the pre-trained model included.
Serve the Model: Start TensorFlow Serving to make predictions accessible.
Containerized Workflow: Use Docker for a hassle-free environment setup.
Detect Disease: Upload an image, and the system will classify it into:
✅ Healthy
⚠️ Early Blight
❌ Late Blight
💡 Why This Project?
🔍 Quick Diagnosis: Save time by identifying diseases with just an image.
🌱 Crop Health: Improve potato yields by addressing issues early.
📊 Scalable Solution: Easily integrate into larger agritech systems.
🛠️ Tech-Stack Expertise: A playground for learning DNN, Docker, and TensorFlow.


🔗 Links & Resources
📝 Documentation: Step-by-step guide to setting up and using the project.

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

Feel free to explore, contribute, or give a ⭐ if you find this project useful. Your support helps grow this initiative!

Happy coding! 💻🚜
