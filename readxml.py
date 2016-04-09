import xml.etree.ElementTree as ET
import glob

fileList1 = glob.glob("DDI_SEMeVAL2013/DrugBank/*.xml")
fileList2 = glob.glob("DDI_SEMeVAL2013/MedLine/*.xml")

fileList = fileList1 + fileList2

#fileList = ['../DDI_SEMeVAL2013/DrugBank/Abarelix_ddi.xml']

cnt = 0
for fname in fileList:
  tree = ET.parse(fname)
  doc = tree.getroot()
  cnt += 1
  for sent in doc:
	text = sent.attrib['text']
	print fname +" "+ sent.attrib['id']
	print text.replace('\n', ' ').strip()
	entity_list = []
	interact_list = []

	for entity_pair in sent:		
		if(entity_pair.tag == 'entity'):
			eid = entity_pair.attrib['id'] 
			place = entity_pair.attrib['charOffset'] 
			etype = entity_pair.attrib['type'] 
			etext = entity_pair.attrib['text']
			print eid+"|"+place+"|"+etype+"|"+etext

	print '\n'

 
