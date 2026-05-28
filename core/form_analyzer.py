from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class FormFeedback:
    severity:str
    message:str
    
    
class FormAnalyzer(ABC):
    @abstractmethod 
    def analyse(self,angles):
        pass
    
class PlankAnalyzer(FormAnalyzer):
    def analyse(self,angles):
        feedback=[]
        if angles["hip"] < 160:
            feedback.append(FormFeedback(
                severity="warning",
                message="Keep your hips up!"))
        if angles["hip"] > 200:
            feedback.append(FormFeedback(
                severity="warning",
                message="Keep your hips down"))
        if angles["shoulder"] < 160:
            feedback.append(FormFeedback(
                severity="warning",
                message="Keep your shoulders back"))
        return feedback
    
class BicepCurlAnalyzer(FormAnalyzer):
    def analyse(self,angles):
        feedback=[]
        if angles["elbow"] > 50:
            feedback.append(FormFeedback(
                severity="warning",
                message="Keep your elbows in,Incomplete curl"))
        if angles["shoulder_abduction"] > 30:
            feedback.append(FormFeedback(
                severity="warning",
                message="Keep your shoulders back,Don't swing your body"))
        
        return feedback
    
    
ANALYZERS = {"plank":PlankAnalyzer(), 
             "bicep_curl": BicepCurlAnalyzer() 
            }