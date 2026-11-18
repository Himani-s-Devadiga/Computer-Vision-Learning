# RNN, LSTM and CTC

## 1. RNN Fundamentals
- **Recurrent Neural Network (RNN):** A neural network designed to process sequential data by using information from previous time steps.
- **Hidden State:** Maintains information from previous inputs to help process the current input.
- **Sequential Processing:** Processes information step by step, making RNNs useful for sequence-based tasks.

## 2. LSTM Architecture
- **Long Short-Term Memory (LSTM):** An advanced RNN architecture designed to learn long-term dependencies.
- **Forget Gate:** Decides which information should be removed.
- **Input Gate:** Controls which new information should be stored.
- **Output Gate:** Determines what information is passed forward.
- **Cell State:** Carries important information across time steps.

## 3. Bidirectional LSTM (BiLSTM)
- Processes sequences in both forward and backward directions.
- Captures context from both previous and future elements.
- Helps improve sequence recognition by understanding surrounding character information.

## 4. CTC Loss
- **Connectionist Temporal Classification (CTC):** A loss function used when input sequences and target text do not have exact alignment.
- **Blank Token:** Represents no character at a particular time step.
- **CTC Alignment:** Allows multiple possible paths to represent the same target sequence.
- **Repeated Characters:** Consecutive repeated characters are collapsed during decoding.

## 5. CTC Decoding

Converts character probability sequences into readable text.

### Greedy Decoding
- Selects the most probable character at each time step.
- Collapses consecutive repeated characters.
- Removes blank tokens.
- Simple and computationally efficient.

### Beam Search Decoding
- Maintains multiple candidate sequences.
- Uses beam width to control the number of retained candidates.
- Tracks blank and non-blank probabilities.
- Handles repeated characters using CTC prefix rules.
- Selects the most probable final sequence.

## 6. Greedy vs. Beam Search
- Compared both decoding approaches using sample probability sequences.
- Observed how different decoding strategies process character probabilities.
- Understood the difference between selecting individual best predictions and exploring multiple candidate sequences.

## 7. Practical Implementation
- Implemented a CTC greedy decoder.
- Implemented a CTC prefix beam search decoder.
- Tested blank token and repeated-character handling.
- Compared greedy and beam search outputs using Python.

### Tools & Technologies
- Python
- NumPy
- PyTorch – planned for CRNN architecture implementation
