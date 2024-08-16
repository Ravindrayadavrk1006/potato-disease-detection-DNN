import React, { useState } from "react";
import Dropzone from "react-dropzone";
import axios from "axios";

function App() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const onDrop = (acceptedFiles) => {
    const formData = new FormData();
    formData.append("file", acceptedFiles[0]);

    axios.post("http://localhost:8000/predict", formData)
      .then((response) => {
        setResult(response.data);
        console.log(response.data)
        setError(null);
      })
      .catch((err) => {
        setError("Error in processing the image");
        setResult(null);
      });
  };

  return (
    <div style={{ padding: "50px", textAlign: "center" }}>
      <h2>Potato Disease Detection</h2>
      <Dropzone onDrop={onDrop} accept="image/*" multiple={false}>
        {({ getRootProps, getInputProps }) => (
          <div
            {...getRootProps()}
            style={{
              border: "2px dashed #0087F7",
              borderRadius: "5px",
              padding: "20px",
              cursor: "pointer",
              width: "300px",
              margin: "0 auto"
            }}
          >
            <input {...getInputProps()} />
            <p>Drag & drop an image here, or click to select one</p>
          </div>
        )}
      </Dropzone>
      {result && (
        <section style={{ marginTop: "20px" , color: "green"}}>
          <h3>Result:</h3>
          <p>{result.class}</p>
          <p>{result.confidence}</p>
        </section>
      )}
      {error && (
        <div style={{ marginTop: "20px", color: "red" }}>
          <p>{error}</p>
        </div>
      )} 
    </div>
  );
}

export default App;
