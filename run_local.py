import cv2
import glob
import os
from utils.classifier import load_model, classify

# Load model and class labels
model, class_names = load_model()

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Process all images in input folder
for img_path in glob.glob('input/*.jpg'):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Skipped: {img_path} (not a valid image)")
        continue

    print(f"Classifying: {img_path}")
    label = classify(model, img, class_names)

    # Add label on image
    cv2.putText(img, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display image
    cv2.imshow(f"{label}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save output
    filename = os.path.basename(img_path)
    output_path = os.path.join('output', f"labeled_{filename}")
    cv2.imwrite(output_path, img)
    print(f"Saved to: {output_path}")
