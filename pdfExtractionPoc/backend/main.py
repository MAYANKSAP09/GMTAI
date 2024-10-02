from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pdb
import pdfplumber
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

@app.post("/process_invoice/")
async def process_invoice(file: UploadFile = File(...)):
    try:
        # Read the contents of the file
      # Set a breakpoint
        contents = await file.read()
        

        r =0

        t = 200

        y =99
       
        # You can process the contents as needed, e.g., parsing a PDF or CSV
        # For demonstration, let's just return the filename and size
        return JSONResponse(content={
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(contents)
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




# @app.post("/process_invoice/")
# async def process_invoice(file: UploadFile = File(...)):
#     try:
#         text = extract_invoice_text(file)
#         extracted_fields = extract_fields_from_text(text)

        # Generate embedding using OpenAI's embedding model
        # embedding = get_embedding(json.dumps(extracted_fields))
        # print(extracted_fields)
        
        # Insert invoice data into PostgreSQL
        # insert_invoice_data_to_db({
        #     'vendor_name': extracted_fields.get("vendor_name"),
        #     'invoice_number': extracted_fields.get("invoice_number"),
        #     'vector': embedding,
        #     'extracted_data': extracted_fields  # Save the extracted data as JSON
        # })

        # return {"message": "Invoice processed and stored successfully."}
        # Explicitly return the extracted data in the response
    #     return {"message": "Invoice processed and stored successfully.", "extracted_data": extracted_fields}        
    # except HTTPException as e:
    #     raise e
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail="An unexpected error occurred while processing the invoice.")

    