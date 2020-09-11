#! /usr/bin/python3

import datetime
#import time
import pyxb
import IEC62559
##import xmlschema ##is_valid+validate
import xml.dom.minidom
from openpyxl import load_workbook
import sys

#lista ig:  1-3,7,13,17,20,25,28,37,39,40,47,55,56,57,65,75,80-86,87,90,91-93
#multi_ele_ini: 8-12,21-24,26-27,38,41-46,48-54,58-64,66-74,76-79
#optionals: 81-86(multi?),91-92(multi?)
def main(filename):
  list_ign = [1,2,3,7,13,17,20,25,28,37,42,43,50,59,60,61,69,80,85,92,95]
  list_opt = [86,87,88,89,90,91,93,94,96,97,98]
  list_multi = [[8,9,10,11,12],[21,22,23,24],[26],[27],[36],[38,39,40,41],[44,45],[46,47,48,49],[51,52,53,54,55,56,57,58],[62,63,64,65,66,67,68],[70,71,72,73,74,75,76,77,78,79],[81,82,83,84]]
  list_ign += list_opt ##borrar+adelante

  #my_xsd = xmlschema.XMLSchema('IEC62559-3_pretty.xsd')
  #my_xsd.is_valid('output.xml')
  #my_xsd.validate('output.xml')
  usecaserep    = IEC62559.UseCaseRepository()
  usecaselib    = IEC62559.UseCaseLibrary()
  usecase       = IEC62559.UseCase()
  version       = IEC62559.Version()
  arealib       = IEC62559.AreaLibrary()
  area          = IEC62559.Area()
  author        = IEC62559.Author()
  relobj        = IEC62559.Objective()
  refobj        = IEC62559.Ref_Objective()
  refusecase    = IEC62559.Ref_UseCase()
  bcase         = IEC62559.Ref_BusinessCase()
  narrative     = IEC62559.Narrative()
  kpi           = IEC62559.KeyPerformanceIndicator()
  assumption    = IEC62559.Assumption()
  condition     = IEC62559.Condition()
  remark        = IEC62559.Remark()
  drawing       = IEC62559.Drawing()
  resourcestr   = IEC62559.Resource_String()
  actorgrouping = IEC62559.ActorGrouping()
  actor         = IEC62559.Actor()
  actorlib      = IEC62559.ActorLibrary()
  reference     = IEC62559.Reference()
  scenario      = IEC62559.Scenario()
  activity      = IEC62559.Activity()
  triggevent    = IEC62559.TriggeringEvent()
  reqlib        = IEC62559.RequirementLibrary()
  reqcat        = IEC62559.RequirementCategory()
  requirement   = IEC62559.Requirement()
  #commonterm    = IEC62559.CommonTerm()
  #custominfo    = IEC62559.CustomInformation()

  wb = load_workbook(filename)
  sheet_list = wb.sheetnames

  IniCol = 3
  col = IniCol

  nstep = "0"
  for sheet in wb:
    sheet_ranges = wb[sheet.title]
    sind = sheet_list.index(sheet.title)

    ind = 1
    while (ind <= 93):
      multi = False
      if (ind not in list_ign):
        for j in range(len(list_multi)):
          if (ind in list_multi[j]):
            multi = True
            ini = list_multi[j][0]
            fin = list_multi[j][-1]
            while (sheet_ranges.cell(row = ind, column = col).value not in [None,'None','']):
              for k in range(fin-ini+1):
                #print(sheet_ranges.cell(row = ind+k, column = col).value)
                cell = str(sheet_ranges.cell(row = ind+k, column = col).value)
                if (ind+k == 8):
                  version.number = cell
                if (ind+k == 9):
                  tdate = cell
                  #print (cell)
                  tdate = tdate[:-9]
                  version.date = datetime.datetime.strptime(tdate, "%Y-%m-%d")
                if (ind+k == 10):
                  author.name = cell
                  version.Author.append(author)
                  author = IEC62559.Author()
                if (ind+k == 11):
                  version.changes = cell
                if (ind+k == 12):
                  version.approvalStatus = cell
                  usecase.Version.append(version)
                  version = IEC62559.Version()

                if (ind+k == 21):
                  kpi.identifier = cell
                if (ind+k == 22):
                  kpi.name = cell
                if (ind+k == 23):
                  kpi.description = cell
                if (ind+k == 24):
                  refobj.mRID = cell
                  kpi.Objective.append(refobj)
                  usecase.KeyPerformanceIndicator.append(kpi)
                  kpi = IEC62559.KeyPerformanceIndicator()
                  refobj = IEC62559.Ref_Objective()

                if (ind+k == 26):
                  assumption.description = cell
                  usecase.Assumption.append(assumption)
                  assumption = IEC62559.Assumption()

                if (ind+k == 27):
                  condition.description = cell
                  usecase.Prerequisite.append(condition)
                  condition = IEC62559.Condition()
                
                if (ind+k == 36):
                  remark.description = cell
                  usecase.Remark.append(remark)
                  remark = IEC62559.Remark()
                
                if (ind+k == 38):
                  drawing.name = cell
                if (ind+k == 39):
                  drawing.drawingType = cell
                if (ind+k == 40):
                  ##drawing.URI.type = cell
                  resourcestr.type = cell
                if (ind+k == 41):
                  drawing.URI = resourcestr
                  usecase.Drawing.append(drawing)
                  drawing = IEC62559.Drawing()
                  resourcestr = IEC62559.Resource_String()

                if (ind+k == 44):
                  actorgrouping.name = cell
                if (ind+k == 45):
                  actorgrouping.description = cell
                  usecase.append(actorgrouping)
                  actorgrouping = IEC62559.ActorGrouping()

                if (ind+k == 46):
                  actor.name = cell
                if (ind+k == 47):
                  actor.type = cell
                if (ind+k == 48):
                  actor.description = cell
                  actorlib.append(actor)
                  actor = IEC62559.Actor()
                #if (ind+k == 49):

                if (ind+k == 51):
                  reference.name = cell
                if (ind+k == 52):
                  reference.number = cell
                if (ind+k == 53):
                  reference.type = cell
                if (ind+k == 54):
                  reference.description = cell
                if (ind+k == 55):
                  reference.status = cell
                if (ind+k == 56):
                  reference.impact = cell
                if (ind+k == 57):
                  reference.originatorOrganization = cell
                if (ind+k == 58):
                  reference.link = cell
                  #reference.name = "reference_name"
                  usecase.Reference.append (reference)
                  reference = IEC62559.Reference()

                if (ind+k == 62):
                  scenario.number = cell
                if (ind+k == 63):
                  scenario.name = cell
                if (ind+k == 64):
                  scenario.description = cell
                #if (ind+k == 65):
                if (ind+k == 66):
                  triggevent.description = cell
                  scenario.TriggeringEvent.append(triggevent)
                  triggevent = IEC62559.TriggeringEvent()
                if (ind+k == 67):
                  condition.description = cell
                  scenario.Precondition.append(condition)
                  condition = IEC62559.Condition()
                if (ind+k == 68):
                  condition.description = cell
                  scenario.Postcondition.append(condition)
                  condition = IEC62559.Condition()
                  usecase.Scenario.append(scenario)
                  scenario = IEC62559.Scenario()

                #if (ind+k == 70):
                if (ind+k == 71):
                  activity.number = cell
                if (ind+k == 72):
                  activity.event = cell
                if (ind+k == 73):
                  activity.name = cell
                if (ind+k == 74):
                  activity.description = cell
                if (ind+k == 75):
                  activity.service = cell
                #if (ind+k == 76):
                #if (ind+k == 77):
                #if (ind+k == 78):
                if (ind+k == 79):
                  nstep = cell
                  for n in usecase.Scenario:
                    if str(n.number) == nstep:
                      n.Activity.append(activity)
                  activity = IEC62559.Activity()

                if (ind+k == 81):
                  requirement.mRID = cell
                #  reqlib = IEC62559.RequirementLibrary()
                #  reqcat = IEC62559.RequirementCategory()
                if (ind+k == 82):
                  requirement.identifier = cell
                if (ind+k == 83):
                  requirement.name = cell
                if (ind+k == 84):
                  requirement.description = cell
                  reqcat.Requirement.append(requirement)
                  requirement = IEC62559.Requirement()
              col += 1
            ind = fin
            col = IniCol
        if (not multi):
          #print(sheet_ranges.cell(row = ind, column = col).value)
          cell = sheet_ranges.cell(row = ind, column = col).value
          if (ind == 4):
            usecase.identifier = cell
          if (ind == 5):
            area.name = cell
            arealib.Area.append(area)
            usecaserep.AreaLibrary = arealib
            area = IEC62559.Area()
          if (ind == 6):
            usecase.name = cell
          if (ind == 14):
            usecase.scope = cell
          if (ind == 15):
            relobj.name = cell
            usecase.RelatedObjective.append(relobj)
          if (ind == 16):
            bcase.mRID = cell
            usecase.BusinessCase.append(bcase)
          if (ind == 18):
            narrative.shortDescription = cell
          if (ind == 19):
            narrative.completeDescription = cell
            usecase.Narrative = narrative
            narrative = IEC62559.Narrative()
          if (ind == 29):
            refusecase.mRID = cell
            usecase.RelatedUseCase.append(refusecase)
            refusecase = IEC62559.Ref_UseCase()
          if (ind == 30):
            usecase.levelOfDepth = cell
          if (ind == 31):
            usecase.prioritization = cell
          if (ind == 32):
            usecase.classification = cell
          if (ind == 33):
            usecase.nature = cell
          if (ind == 34):
            usecase.keywords = cell
          #if (ind == 35):
          #  usecase. = (sheet_ranges.cell(row = ind, column = col).value)
      ind += 1

    #el break es para leer solo la primera sheet
    break
  usecaselib.UseCase.append(usecase)
  usecaselib.name = "UCL_name"
  usecaserep.UseCaseLibrary = usecaselib
  usecaserep.name = "UCR_name"
  usecaserep.ActorLibrary.append(actorlib)
  reqcat.name = "namen" #sustituir por cell
  reqcat.identifier = "idi"  #sustituir por cell
  reqlib.append(reqcat)
  usecaserep.RequirementLibrary = reqlib

  usecase = IEC62559.UseCase()
  
  ##borrar (asociados con UCR)
  arealib  = IEC62559.AreaLibrary()
  actorlib = IEC62559.ActorLibrary()
  reqlib = IEC62559.RequirementLibrary()
  reqcat = IEC62559.RequirementCategory()

  #print(usecaselib.toxml("utf-8", element_name='UseCaseLibrary').decode('utf-8'))
  #print(xml.dom.minidom.parseString(usecaselib.toxml("utf-8", element_name='UseCaseLibrary').decode('utf-8')).toprettyxml())
  print(xml.dom.minidom.parseString(usecaserep.toxml("utf-8", element_name='UseCaseRepository').decode('utf-8')).toprettyxml())

#Python3
if len(sys.argv) < 2:
    print("I require one parameter, which should be the name of the file to process.")
    sys.exit(1)
filename = sys.argv[1]
print("Processing ", filename)
main(filename)
