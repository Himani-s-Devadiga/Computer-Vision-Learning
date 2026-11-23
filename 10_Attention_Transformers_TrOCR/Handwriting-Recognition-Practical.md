# Handwriting Recognition Practical Using TrOCR

## Objective

To implement handwritten text recognition using a pretrained TrOCR model and evaluate its predictions against reference text.

## Model Used

`microsoft/trocr-base-handwritten`

The pretrained model was used for inference. The model was not fine-tuned during this experiment.

## Tools and Libraries

- Python
- PyTorch
- Hugging Face Transformers
- Pillow
- JiWER

## Implementation Steps

1. Install the required Python libraries.
2. Load the pretrained TrOCR processor and model.
3. Prepare a handwritten sample image.
4. Pass the image to the TrOCR model.
5. Generate predicted text.
6. Compare the prediction with the reference text.
7. Evaluate recognition using Word Error Rate (WER) and Character Error Rate (CER).

## Image Segmentation

The original handwritten image contained multiple text lines.

The full-image prediction was poor, so the image was cropped into two individual text lines to evaluate line-level recognition.

## Experiment Results

Reference text:

`This is a sample of my handwriting`

### Full-image inference

- Prediction: `The first way in an advertising .`
- Raw WER: 100%
- Raw CER: 67.65%

### Line-level inference

| Metric | Line 1 | Line 2 |
|---|---:|---:|
| Reference | This is a sample | of my handwriting. |
| Prediction | This is a sample | of my handwriting . |
| Raw WER | 0% | 66.67% |
| Raw CER | 0% | 5.56% |

### Combined line-level evaluation

- Raw WER: 28.57%
- Raw CER: 2.86%
- Punctuation-normalized WER: 0%
- Punctuation-normalized CER: 0%

**Note:** Punctuation normalization removes punctuation before comparison. Therefore, the normalized scores do not mean the original predictions were completely identical.

## Observations

- Line-level image segmentation improved recognition significantly compared with full-image inference.
- The first line was recognized exactly.
- The second line contained a punctuation spacing difference.
- Preprocessing and segmentation are important for handwriting recognition.
- Evaluation should consider both raw and normalized error rates.

## Limitations

- The experiment used a small handwritten sample.
- The pretrained model was not fine-tuned.
- Results may differ for other handwriting styles.
- Handwritten medical prescriptions require additional validation.

## Conclusion

This practical demonstrated handwritten text recognition using a pretrained TrOCR model.

It also showed the importance of image segmentation and evaluation using WER and CER.

For medical prescription recognition, extracted medicine names, dosages, frequencies, and durations must be verified by a qualified human reviewer. OCR output must not be treated as medical advice.
