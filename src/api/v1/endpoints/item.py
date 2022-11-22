from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
import shutil
import uuid

from src.model.yolov5.object_detection_model import ObjectDetectionModel, save_results_to

model_instance = ObjectDetectionModel()

router = APIRouter(
    prefix="/items",
    tags=["Inventory items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/detect")
async def inventory_item_detection(image_file: UploadFile):
    generated_image_name = str(uuid.uuid4())
    file_type = image_file.filename.split(".")[-1]
    image_name = f"{generated_image_name}.{file_type}"
    base_image_path = "images/"
    requested_image_path = f"{base_image_path}requested/{image_name}"
    guessed_images_dir = f"{base_image_path}guessed"
    with open(requested_image_path, "wb") as buffer:
        shutil.copyfileobj(image_file.file, buffer)
        buffer.close()
    result = model_instance.predict(requested_image_path)
    save_results_to(result, guessed_images_dir, image_name)
    guessed_image_path = f"{guessed_images_dir}/{image_name}"
    return FileResponse(guessed_image_path)
