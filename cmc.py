def accuracy_score(TP,TN,total_predictions):
    result = (TP + TN )/total_predictions
    print(f'The accuracy of the model is {result}')

def recall(TP,FN):
    result = TP/(TP+FN)
    print(f'The recall of the model is {result}')

def specificity(TN,FP):
    result = TN/(TN+FP)
    print(f'The specificity of the model is {result}')

def precision(TP,FP):
    result = TP/(TP+FP)
    print(f'The precision of the model is {result}')
