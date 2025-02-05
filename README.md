# kafka Image Processing with Thumbnails

In this branch, I have demonstrated an image upload, processing, and thumbnail generation system using kafka.

- **Producer (kafka)**: 
  - Created a producer that sends image metadata (path and name) to a Kafka topic for processing.
  
- **Consumer (kafka)**: 
  - Developed a consumer that listens to Kafka, processes the image (by generating a thumbnail), and saves it with the same name as the original image.
  
- **Streamlit App**:
  - Built a Streamlit app that allows users to upload images.
  - Once uploaded, the app sends the image to Kafka for processing.
  - The app displays the original image along with its generated thumbnail after processing.

## Running the Application

1. **Kafka Setup**: 
   - Ensure Kafka is running on `localhost:9092`.

2. **Start Consumer**:  
   ```bash
   python consumers.py
   ```
4. **Start Streamlit app**:
   ```bash
   streamlit run app.py
   ```

