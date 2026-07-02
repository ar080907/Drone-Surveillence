from ultralytics import YOLO

def main():
    model = YOLO("best.pt")

    results = model.train(
        data="dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=2,
        workers=2,
        device="cpu",
        project="runs",
        name="drone_detector",
        patience=20,
        verbose=True,
        lr0=0.0001,
        cache=True
    )

    print("Training complete!")

if __name__ == "__main__":
    main()