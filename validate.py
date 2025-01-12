from tensorflow import keras
import tensorflow_text as text  # this import may seem unused but is necessary

from models import SVM
from resources import validate_config as config
from utils.evaluate import evaluate_model
from utils.text_processing import load_dataset


def validate():
    validate_dataset, classes = load_dataset(config.DATASET_LOCATION, config.CLEAN_TEXT)

    if config.BERT["ENABLED"]:
        BERT_model = keras.models.load_model(config.BERT['MODEL_LOCATION'], compile=False)
        y_pred_proba = BERT_model.predict(validate_dataset['text'])
        print('Evaluation of ' + config.BERT['NAME'])
        evaluate_model(y_pred_proba, validate_dataset['label'], classes)

    if config.SVM["ENABLED"]:
        tfidf, SVM_model = SVM.load(config.SVM['MODEL_LOCATION'])
        y_pred = SVM.predict(tfidf, SVM_model, validate_dataset['text'])
        print('Evaluation of ' + config.SVM['NAME'])
        evaluate_model(y_pred, validate_dataset['label'], classes)

    if config.CNN["ENABLED"]:
        CNN_model = keras.models.load_model(config.CNN['MODEL_LOCATION'])
        y_pred_proba = CNN_model.predict(validate_dataset['text'])
        print('Evaluation of ' + config.CNN['NAME'])
        evaluate_model(y_pred_proba, validate_dataset['label'], classes)

    if config.RNN["ENABLED"]:
        RNN_model = keras.models.load_model(config.RNN['MODEL_LOCATION'])
        y_pred_proba = RNN_model.predict(validate_dataset['text'])
        print('Evaluation of ' + config.RNN['NAME'])
        evaluate_model(y_pred_proba, validate_dataset['label'], classes)


if __name__ == '__main__':
    validate()
