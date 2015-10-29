import bimserver
import base64
import bimserver
import json
import binascii
client = bimserver.api("thisisanexperimentalserver.com","j.beetz@tue.nl", "hackathon")

# deserializer_id = client.Bimsie1ServiceInterface.getSuggestedDeserializerForExtension(extension="ifc").get('oid')
# project_id = client.Bimsie1ServiceInterface.addProject(projectName="My new project", schema="ifc2x3tc1").get('oid')
# project_id = client.Bimsie1ServiceInterface.addProject(projectName="My new project", schema="ifc2x3tc1").get('oid')
projects = client.ServiceInterface.getAllReadableProjects()
print(projects)

# project_id = client.Bimsie1ServiceInterface.addProject(projectName="aechackathon.nl lora", schema="ifc2x3tc1").get('oid')
project_id = client.Bimsie1ServiceInterface.getProjectsByName(name="aechackathon.nl lora")[0].get('oid')
last_revision_id = client.Bimsie1ServiceInterface.getAllRevisionsOfProject(poid=project_id)[-1].get('oid')
last_revision = client.Bimsie1ServiceInterface.getAllRevisionsOfProject(poid=project_id)[-1]
print(last_revision)
with open("gaslab_table_red.json", 'rb') as f:
    # json_data = json.loads(f.read())
    rawstr = str(f.read())
    # print (rawstr)
    b64 = base64.standard_b64encode()
    # binascii.b2a_base64(b64)
    print (b64)
typeinfo = '''{
 "__type":"SFile",
 "data":"'''+str(b64)+'''"
}'''
file_id=client.ServiceInterface.uploadFile(file=json.loads(typeinfo))
2883656

extendedD = '''{
"__type":"SExtendedData",
"fileId":'''+str(file_id)+''',
"schemaId":262217
}'''

res = client.Bimsie1ServiceInterface.addExtendedDataToRevision(roid=last_revision_id, extendedData=json.loads(extendedD))
print (res)

# deserializer_id = client.Bimsie1ServiceInterface.getSuggestedDeserializerForExtension(extension="ifc", poid=last_revision)
# with open("gaslab.ifc", "rb") as f:
#     ifc_data = f.read()
#
# client.Bimsie1ServiceInterface.checkin(
#     poid=               project_id,
#     comment=            "initial commit hackathon day 1",
#     deserializerOid=    deserializer_id,
#     fileSize=           len(ifc_data),
#     fileName=           "gaslab.ifc",
#     data=               base64.b64encode(ifc_data).decode('utf-8'),
#     sync=               "false"
# )
# client.AdminInterface.regenerateGeometry(croid=last_revision)