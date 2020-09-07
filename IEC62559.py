# ./IEC62559.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ca5c09406a51855b87dbeb76e5f77a5f25dac427
# Generated 2020-07-17 10:08:14.881305 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:aa1f184c-c804-11ea-9041-b42e99d733c1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}DrawingClassification
class DrawingClassification (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """possible types of drawing"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrawingClassification')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 142, 0)
    _Documentation = 'possible types of drawing'
DrawingClassification._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrawingClassification, enum_prefix=None)
DrawingClassification.domain_overview = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='domain overview', tag='domain_overview')
DrawingClassification.use_case_overview = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='use case overview', tag='use_case_overview')
DrawingClassification.documentation = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='documentation', tag='documentation')
DrawingClassification.scenarios_flowchart = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='scenarios flowchart', tag='scenarios_flowchart')
DrawingClassification.scenario_overview = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='scenario overview', tag='scenario_overview')
DrawingClassification.activities_flowchart = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='activities flowchart', tag='activities_flowchart')
DrawingClassification.activity_overview = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='activity overview', tag='activity_overview')
DrawingClassification.business_objects_overview = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='business objects overview', tag='business_objects_overview')
DrawingClassification.other = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
DrawingClassification.role_model = DrawingClassification._CF_enumeration.addEnumeration(unicode_value='role model', tag='role_model')
DrawingClassification._InitializeFacetMap(DrawingClassification._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrawingClassification', DrawingClassification)
_module_typeBindings.DrawingClassification = DrawingClassification

# Atomic simple type: {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Resource_String_value_ValueType
class Resource_String_value_ValueType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Resource_String_value_ValueType')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 218, 0)
    _Documentation = None
Resource_String_value_ValueType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Resource_String_value_ValueType', Resource_String_value_ValueType)
_module_typeBindings.Resource_String_value_ValueType = Resource_String_value_ValueType

# Atomic simple type: {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}ResourceType
class ResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """list of possible resources"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceType')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 221, 0)
    _Documentation = 'list of possible resources'
ResourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResourceType, enum_prefix=None)
ResourceType.image = ResourceType._CF_enumeration.addEnumeration(unicode_value='image', tag='image')
ResourceType.UMLDiagram = ResourceType._CF_enumeration.addEnumeration(unicode_value='UMLDiagram', tag='UMLDiagram')
ResourceType._InitializeFacetMap(ResourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResourceType', ResourceType)
_module_typeBindings.ResourceType = ResourceType

# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Activity with content type ELEMENT_ONLY
class Activity (pyxb.binding.basis.complexTypeDefinition):
    """It may be subdivided into other activities or represent an elementary step of the
scenario."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Activity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 5, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BusinessObject uses Python identifier BusinessObject
    __BusinessObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BusinessObject'), 'BusinessObject', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_BusinessObject', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 11, 0), )

    
    BusinessObject = property(__BusinessObject.value, __BusinessObject.set, None, 'This describes briefly the information to be exchanged between\nthe two actors – information producer and information receiver. It may list several information items in one step, comma\nseparated.')

    
    # Element ChildActivity uses Python identifier ChildActivity
    __ChildActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ChildActivity'), 'ChildActivity', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_ChildActivity', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 19, 0), )

    
    ChildActivity = property(__ChildActivity.value, __ChildActivity.set, None, 'child activities')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 24, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element Drawing uses Python identifier Drawing
    __Drawing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Drawing'), 'Drawing', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_Drawing', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 29, 0), )

    
    Drawing = property(__Drawing.value, __Drawing.set, None, 'the list of associated drawing')

    
    # Element event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event'), 'event', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_event', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 34, 0), )

    
    event = property(__event.value, __event.set, None, 'It is the event that triggers the step. This might be completion of\nprevious steps (in that case the event is the comma-separated list of their numbers) or the condition to exit a\nloop.')

    
    # Element InformationProducer uses Python identifier InformationProducer
    __InformationProducer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InformationProducer'), 'InformationProducer', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_InformationProducer', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 41, 0), )

    
    InformationProducer = property(__InformationProducer.value, __InformationProducer.set, None, 'This identifies the producer or source of the information. Thisshould be one of the actors defined in the repository.')

    
    # Element InformationReceiver uses Python identifier InformationReceiver
    __InformationReceiver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InformationReceiver'), 'InformationReceiver', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_InformationReceiver', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 47, 0), )

    
    InformationReceiver = property(__InformationReceiver.value, __InformationReceiver.set, None, 'This identifies the receiver of the information. This should be one\nof the actors defined in the repository.')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 54, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 59, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_number', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 64, 0), )

    
    number = property(__number.value, __number.set, None, 'index of the activity')

    
    # Element PrimaryActor uses Python identifier PrimaryActor
    __PrimaryActor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PrimaryActor'), 'PrimaryActor', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_PrimaryActor', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 69, 0), )

    
    PrimaryActor = property(__PrimaryActor.value, __PrimaryActor.set, None, 'reference to the PrimaryActor')

    
    # Element Requirement uses Python identifier Requirement
    __Requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Requirement'), 'Requirement', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_Requirement', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 74, 0), )

    
    Requirement = property(__Requirement.value, __Requirement.set, None, 'Several requirements may be listed in one step, comma\nseparated.')

    
    # Element service uses Python identifier service
    __service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Activity_service', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 81, 0), )

    
    service = property(__service.value, __service.set, None, 'This column identifies the nature of the information flow and the\noriginator of the information. Available options are CREATE, GET, CHANGE, DELETE, CANCEL, EXECUTE derived from\nIEC 61968-100:2013.\nAdditionally, REPORT, TIMER and REPEAT are suggested.\n- CREATE means that an information object is to be created at the Producer.\n- GET (this is the default value if none is populated) means that the Receiver requests information from the Producer\n(default).\n- CHANGE means that information is to be updated. Producer updates the Receiver’s information.\n- DELETE means that information is to be deleted. Producer deletes information from the Receiver.\n- CANCEL, CLOSE imply actions related to processes, such as the closure of a work order or the cancellation of a\ncontrol request.\n- EXECUTE is used when a complex transaction is being conveyed using a service, which potentially contains more\nthan one verb.\n- REPORT is used to represent transferral of unsolicited information or asynchronous information flows. Producer\nprovides information to the Receiver.\n- TIMER is used to represent a waiting period. When using the TIMER service, the Information Producer and\nInformation Receiver fields shall refer to the same actor.\n- REPEAT is used to indicate that a series of steps is repeated until a condition or trigger event. The condition is\nspecified as the text in the "Event" column for this row or step. Following the word REPEAT, the first and last step numbers of\nthe series to be repeated shall appear, in parenthesis, in the following form: REPEAT(X-Y) where X is the first step and Y is the\nlast step.\nThese common service definitions are related to automation/information or communication systems. In case the use case\ntemplate is applied in other domains, further services might be used and described.')

    _ElementMap.update({
        __BusinessObject.name() : __BusinessObject,
        __ChildActivity.name() : __ChildActivity,
        __description.name() : __description,
        __Drawing.name() : __Drawing,
        __event.name() : __event,
        __InformationProducer.name() : __InformationProducer,
        __InformationReceiver.name() : __InformationReceiver,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __number.name() : __number,
        __PrimaryActor.name() : __PrimaryActor,
        __Requirement.name() : __Requirement,
        __service.name() : __service
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Activity = Activity
Namespace.addCategoryObject('typeBinding', 'Activity', Activity)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Drawing with content type ELEMENT_ONLY
class Drawing (pyxb.binding.basis.complexTypeDefinition):
    """For clarification, in general it is recommended to provide drawing(s) by hand, by
a graphic or as UML graphics (preferred in IEC 62559). The drawing should show interactions which identify the steps where
possible."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Drawing')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 110, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element drawingType uses Python identifier drawingType
    __drawingType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'drawingType'), 'drawingType', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Drawing_drawingType', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 117, 0), )

    
    drawingType = property(__drawingType.value, __drawingType.set, None, 'type of drawing')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Drawing_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 121, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Drawing_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 126, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element URI uses Python identifier URI
    __URI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URI'), 'URI', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Drawing_URI', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 131, 0), )

    
    URI = property(__URI.value, __URI.set, None, 'resource Path to an image file\nex: http://www..../image.jpg\nor\npath to an XMI file with a relative diagram path from the root of the UML model. ex:\nhttp://www.../Model.xmi#Package1/Package2/.../DiagName')

    _ElementMap.update({
        __drawingType.name() : __drawingType,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __URI.name() : __URI
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Drawing = Drawing
Namespace.addCategoryObject('typeBinding', 'Drawing', Drawing)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_Requirement with content type ELEMENT_ONLY
class Ref_Requirement (pyxb.binding.basis.complexTypeDefinition):
    """requirement of a part of the use case"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_Requirement')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 238, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_Requirement_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 243, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_Requirement = Ref_Requirement
Namespace.addCategoryObject('typeBinding', 'Ref_Requirement', Ref_Requirement)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_Actor with content type ELEMENT_ONLY
class Ref_Actor (pyxb.binding.basis.complexTypeDefinition):
    """It is the entity that communicates and interacts.
These actors can include people, software applications, systems, databases, and even the power system
itself."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_Actor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 250, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_Actor_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 257, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_Actor = Ref_Actor
Namespace.addCategoryObject('typeBinding', 'Ref_Actor', Ref_Actor)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_BusinessObject with content type ELEMENT_ONLY
class Ref_BusinessObject (pyxb.binding.basis.complexTypeDefinition):
    """business object exchanged in detailed activity steps"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_BusinessObject')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 264, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_BusinessObject_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 269, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_BusinessObject = Ref_BusinessObject
Namespace.addCategoryObject('typeBinding', 'Ref_BusinessObject', Ref_BusinessObject)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Actor with content type ELEMENT_ONLY
class Actor (pyxb.binding.basis.complexTypeDefinition):
    """It is the entity that communicates and interacts.
These actors can include people, software applications, systems, databases, and even the power system
itself."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Actor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 275, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Actor_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 282, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Actor_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 287, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Actor_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 292, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Actor_type', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 297, 0), )

    
    type = property(__type.value, __type.set, None, 'type of the actor (business, system, ...)')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Actor = Actor
Namespace.addCategoryObject('typeBinding', 'Actor', Actor)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}ActorGrouping with content type ELEMENT_ONLY
class ActorGrouping (pyxb.binding.basis.complexTypeDefinition):
    """group of actors used to organize an actor list"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActorGrouping')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 304, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_ActorGrouping_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 309, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element FurtherActorInformation uses Python identifier FurtherActorInformation
    __FurtherActorInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FurtherActorInformation'), 'FurtherActorInformation', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_ActorGrouping_FurtherActorInformation', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 314, 0), )

    
    FurtherActorInformation = property(__FurtherActorInformation.value, __FurtherActorInformation.set, None, 'In a context of one use case, an actor grouped into an\nActorGrouping may have one FurtherActorInformation.')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_ActorGrouping_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 321, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_ActorGrouping_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 326, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __description.name() : __description,
        __FurtherActorInformation.name() : __FurtherActorInformation,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActorGrouping = ActorGrouping
Namespace.addCategoryObject('typeBinding', 'ActorGrouping', ActorGrouping)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}FurtherActorInformation with content type ELEMENT_ONLY
class FurtherActorInformation (pyxb.binding.basis.complexTypeDefinition):
    """Individual or additional information that relates to the use case can be
provided."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FurtherActorInformation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 333, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Actor uses Python identifier Actor
    __Actor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Actor'), 'Actor', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_FurtherActorInformation_Actor', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 339, 0), )

    
    Actor = property(__Actor.value, __Actor.set, None, 'information related to an actor')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_FurtherActorInformation_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 344, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_FurtherActorInformation_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 348, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __Actor.name() : __Actor,
        __description.name() : __description,
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FurtherActorInformation = FurtherActorInformation
Namespace.addCategoryObject('typeBinding', 'FurtherActorInformation', FurtherActorInformation)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}ActorLibrary with content type ELEMENT_ONLY
class ActorLibrary (pyxb.binding.basis.complexTypeDefinition):
    """actors of the repository"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActorLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 355, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Actor uses Python identifier Actor
    __Actor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Actor'), 'Actor', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_ActorLibrary_Actor', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 360, 0), )

    
    Actor = property(__Actor.value, __Actor.set, None, 'the actors listed in the library')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_ActorLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 365, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __Actor.name() : __Actor,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActorLibrary = ActorLibrary
Namespace.addCategoryObject('typeBinding', 'ActorLibrary', ActorLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Area with content type ELEMENT_ONLY
class Area (pyxb.binding.basis.complexTypeDefinition):
    """area of knowledge or activity characterized by a set of concepts and terminology
understood by the practitioners in that area"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Area')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 372, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Area_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 378, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Area_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 383, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Area_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 388, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Area = Area
Namespace.addCategoryObject('typeBinding', 'Area', Area)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Author with content type ELEMENT_ONLY
class Author (pyxb.binding.basis.complexTypeDefinition):
    """This field is used to document who has provided the current version. It can be a
person, organization or, for example, standardization committee like a technical committee (TC) or working group
(WG)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Author')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 395, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Author_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 402, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Author_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 407, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Author = Author
Namespace.addCategoryObject('typeBinding', 'Author', Author)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}BusinessCase with content type ELEMENT_ONLY
class BusinessCase (pyxb.binding.basis.complexTypeDefinition):
    """It provides a description or reference with some rationale for the suggested use
case. Usually the business case is related to several use cases."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessCase')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 414, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Area uses Python identifier Area
    __Area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Area'), 'Area', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessCase_Area', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 420, 0), )

    
    Area = property(__Area.value, __Area.set, None, 'Use cases can be used in various areas (e.g. energy system).Within these areas different domains are used to define / determine a more specific subgrouping. One or more domains and\nzones, comma separated, can be specified in the template.')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessCase_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 426, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessCase_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 431, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessCase_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 436, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __Area.name() : __Area,
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BusinessCase = BusinessCase
Namespace.addCategoryObject('typeBinding', 'BusinessCase', BusinessCase)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_Area with content type ELEMENT_ONLY
class Ref_Area (pyxb.binding.basis.complexTypeDefinition):
    """area of knowledge or activity characterized by a set of concepts and terminology
understood by the practitioners in that area"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_Area')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 443, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_Area_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 449, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_Area = Ref_Area
Namespace.addCategoryObject('typeBinding', 'Ref_Area', Ref_Area)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}BusinessCaseLibrary with content type ELEMENT_ONLY
class BusinessCaseLibrary (pyxb.binding.basis.complexTypeDefinition):
    """business cases of the repository"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessCaseLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 456, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BusinessCase uses Python identifier BusinessCase
    __BusinessCase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BusinessCase'), 'BusinessCase', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessCaseLibrary_BusinessCase', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 461, 0), )

    
    BusinessCase = property(__BusinessCase.value, __BusinessCase.set, None, 'the list of business cases')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessCaseLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 466, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __BusinessCase.name() : __BusinessCase,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BusinessCaseLibrary = BusinessCaseLibrary
Namespace.addCategoryObject('typeBinding', 'BusinessCaseLibrary', BusinessCaseLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}BusinessObject with content type ELEMENT_ONLY
class BusinessObject (pyxb.binding.basis.complexTypeDefinition):
    """business object exchanged in detailed activity steps"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessObject')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 473, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObject_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 478, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObject_identifier', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 483, 0), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'identification used in references in the use case\ndescription')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObject_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 489, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObject_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 494, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element Requirement uses Python identifier Requirement
    __Requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Requirement'), 'Requirement', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObject_Requirement', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 498, 0), )

    
    Requirement = property(__Requirement.value, __Requirement.set, None, 'It can be used to define requirements related to the information\nand not to the step as in the step by step analysis.')

    _ElementMap.update({
        __description.name() : __description,
        __identifier.name() : __identifier,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __Requirement.name() : __Requirement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BusinessObject = BusinessObject
Namespace.addCategoryObject('typeBinding', 'BusinessObject', BusinessObject)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}BusinessObjectLibrary with content type ELEMENT_ONLY
class BusinessObjectLibrary (pyxb.binding.basis.complexTypeDefinition):
    """business objects which are exchanged in use cases"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessObjectLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 506, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BusinessObject uses Python identifier BusinessObject
    __BusinessObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BusinessObject'), 'BusinessObject', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObjectLibrary_BusinessObject', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 511, 0), )

    
    BusinessObject = property(__BusinessObject.value, __BusinessObject.set, None, 'list of business objects within the library')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_BusinessObjectLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 516, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __BusinessObject.name() : __BusinessObject,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BusinessObjectLibrary = BusinessObjectLibrary
Namespace.addCategoryObject('typeBinding', 'BusinessObjectLibrary', BusinessObjectLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}CommonTerm with content type ELEMENT_ONLY
class CommonTerm (pyxb.binding.basis.complexTypeDefinition):
    """It represents a glossary term and its definition."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonTerm')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 523, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CommonTerm_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 528, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CommonTerm_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 533, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CommonTerm_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 538, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonTerm = CommonTerm
Namespace.addCategoryObject('typeBinding', 'CommonTerm', CommonTerm)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}CommonTermLibrary with content type ELEMENT_ONLY
class CommonTermLibrary (pyxb.binding.basis.complexTypeDefinition):
    """common glossary defining terms for all use cases"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonTermLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 545, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CommonTerm uses Python identifier CommonTerm
    __CommonTerm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CommonTerm'), 'CommonTerm', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CommonTermLibrary_CommonTerm', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 550, 0), )

    
    CommonTerm = property(__CommonTerm.value, __CommonTerm.set, None, 'list of common terms')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CommonTermLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 555, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __CommonTerm.name() : __CommonTerm,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CommonTermLibrary = CommonTermLibrary
Namespace.addCategoryObject('typeBinding', 'CommonTermLibrary', CommonTermLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Condition with content type ELEMENT_ONLY
class Condition (pyxb.binding.basis.complexTypeDefinition):
    """It describes either a precondition or a postcondition."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Condition')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 562, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Condition_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 567, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Condition_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 571, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Condition_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 576, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Condition_number', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 581, 0), )

    
    number = property(__number.value, __number.set, None, 'index of the condition')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __number.name() : __number
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Condition = Condition
Namespace.addCategoryObject('typeBinding', 'Condition', Condition)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}CustomInformation with content type ELEMENT_ONLY
class CustomInformation (pyxb.binding.basis.complexTypeDefinition):
    """It provides a flexible option to include miscellaneous custom, semi-structured
information which does not fit into other parts of the template."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomInformation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 588, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element key uses Python identifier key
    __key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CustomInformation_key', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 594, 0), )

    
    key = property(__key.value, __key.set, None, 'unique key for identification purposes')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CustomInformation_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 599, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reference'), 'reference', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CustomInformation_reference', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 604, 0), )

    
    reference = property(__reference.value, __reference.set, None, 'This field refers to relevant template\nsection.')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_CustomInformation_value', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 610, 0), )

    
    value_ = property(__value.value, __value.set, None, 'the corresponding information for the provided\nkey')

    _ElementMap.update({
        __key.name() : __key,
        __mRID.name() : __mRID,
        __reference.name() : __reference,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CustomInformation = CustomInformation
Namespace.addCategoryObject('typeBinding', 'CustomInformation', CustomInformation)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}KeyPerformanceIndicator with content type ELEMENT_ONLY
class KeyPerformanceIndicator (pyxb.binding.basis.complexTypeDefinition):
    """Key Performance Indicator (KPI) related to the objectives of the use
case"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeyPerformanceIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 618, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_KeyPerformanceIndicator_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 624, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_KeyPerformanceIndicator_identifier', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 629, 0), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'unique identifier for the Key Performance Indicator\n(KPI)')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_KeyPerformanceIndicator_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 635, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_KeyPerformanceIndicator_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 640, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element Objective uses Python identifier Objective
    __Objective = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Objective'), 'Objective', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_KeyPerformanceIndicator_Objective', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 645, 0), )

    
    Objective = property(__Objective.value, __Objective.set, None, 'the related objective')

    _ElementMap.update({
        __description.name() : __description,
        __identifier.name() : __identifier,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __Objective.name() : __Objective
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.KeyPerformanceIndicator = KeyPerformanceIndicator
Namespace.addCategoryObject('typeBinding', 'KeyPerformanceIndicator', KeyPerformanceIndicator)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_Objective with content type ELEMENT_ONLY
class Ref_Objective (pyxb.binding.basis.complexTypeDefinition):
    """objective of the use case"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_Objective')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 651, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_Objective_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 656, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_Objective = Ref_Objective
Namespace.addCategoryObject('typeBinding', 'Ref_Objective', Ref_Objective)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Narrative with content type ELEMENT_ONLY
class Narrative (pyxb.binding.basis.complexTypeDefinition):
    """It describes the narrative of the use case."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Narrative')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 663, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element completeDescription uses Python identifier completeDescription
    __completeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'completeDescription'), 'completeDescription', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Narrative_completeDescription', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 668, 0), )

    
    completeDescription = property(__completeDescription.value, __completeDescription.set, None, 'It provides a complete narrative of the use case from a user’s\npoint of view, describing what occurs when, why, with what expectation, and under what conditions. This narrative should be\nwritten in plain text so that non-domain experts can understand it.\nThe length of the complete description can range from a few sentences to a few pages, depending on the complexity and/or\nnewness of the use case. This description often helps the domain expert to reflect on the requirements for the use case before\ngetting into the details in the next sections of the use case template.\nThe description may include drawings for explanation.')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Narrative_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 679, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element shortDescription uses Python identifier shortDescription
    __shortDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shortDescription'), 'shortDescription', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Narrative_shortDescription', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 684, 0), )

    
    shortDescription = property(__shortDescription.value, __shortDescription.set, None, 'It is a short text intended to summarize the main idea as a\nservice for the reader who is searching for a use case or looking for an overview.\nRecommendation: This short description should have not more than 150 words.')

    _ElementMap.update({
        __completeDescription.name() : __completeDescription,
        __mRID.name() : __mRID,
        __shortDescription.name() : __shortDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Narrative = Narrative
Namespace.addCategoryObject('typeBinding', 'Narrative', Narrative)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Objective with content type ELEMENT_ONLY
class Objective (pyxb.binding.basis.complexTypeDefinition):
    """objective of the use case"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Objective')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 693, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Objective_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 698, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Objective_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 703, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Objective_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 708, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Objective = Objective
Namespace.addCategoryObject('typeBinding', 'Objective', Objective)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_BusinessCase with content type ELEMENT_ONLY
class Ref_BusinessCase (pyxb.binding.basis.complexTypeDefinition):
    """It provides a description or reference with some rationale for the suggested use
case. Usually the business case is related to several use cases."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_BusinessCase')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 715, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_BusinessCase_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 721, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_BusinessCase = Ref_BusinessCase
Namespace.addCategoryObject('typeBinding', 'Ref_BusinessCase', Ref_BusinessCase)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_CommonTerm with content type ELEMENT_ONLY
class Ref_CommonTerm (pyxb.binding.basis.complexTypeDefinition):
    """It represents a glossary term and its definition."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_CommonTerm')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 727, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_CommonTerm_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 732, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_CommonTerm = Ref_CommonTerm
Namespace.addCategoryObject('typeBinding', 'Ref_CommonTerm', Ref_CommonTerm)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Ref_UseCase with content type ELEMENT_ONLY
class Ref_UseCase (pyxb.binding.basis.complexTypeDefinition):
    """specification of a set of actions performed by a system, which yields an
observable result that is, typically, of value for one or more actors or other stakeholders of the system """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ref_UseCase')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 739, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Ref_UseCase_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 745, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Ref_UseCase = Ref_UseCase
Namespace.addCategoryObject('typeBinding', 'Ref_UseCase', Ref_UseCase)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Reference with content type ELEMENT_ONLY
class Reference (pyxb.binding.basis.complexTypeDefinition):
    """Any references that might restrict or affect the design, understanding, and
requirements of the use case shall be identified, including contracts, regulations, policies, financial considerations, engineering
constraints, pollution constraints, and other environmental quality issues."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Reference')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 752, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 759, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element impact uses Python identifier impact
    __impact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'impact'), 'impact', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_impact', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 764, 0), )

    
    impact = property(__impact.value, __impact.set, None, 'This information describes the nature of the influence of the\ndocument on the use case.')

    
    # Element link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_link', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 770, 0), )

    
    link = property(__link.value, __link.set, None, 'If available, a public link to the document can be\nprovided.')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 776, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 781, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_number', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 786, 0), )

    
    number = property(__number.value, __number.set, None, 'index of the reference')

    
    # Element originatorOrganization uses Python identifier originatorOrganization
    __originatorOrganization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'originatorOrganization'), 'originatorOrganization', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_originatorOrganization', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 791, 0), )

    
    originatorOrganization = property(__originatorOrganization.value, __originatorOrganization.set, None, 'This describes the name of the organization publishing the\ndocument.')

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_status', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 797, 0), )

    
    status = property(__status.value, __status.set, None, 'status of the referenced document')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Reference_type', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 801, 0), )

    
    type = property(__type.value, __type.set, None, 'There are different reference types (e.g. standard, regulation,\ncontract, others like publications).')

    _ElementMap.update({
        __description.name() : __description,
        __impact.name() : __impact,
        __link.name() : __link,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __number.name() : __number,
        __originatorOrganization.name() : __originatorOrganization,
        __status.name() : __status,
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Reference = Reference
Namespace.addCategoryObject('typeBinding', 'Reference', Reference)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Remark with content type ELEMENT_ONLY
class Remark (pyxb.binding.basis.complexTypeDefinition):
    """It is used for further comments which are not considered
elsewhere."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Remark')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 809, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Remark_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 815, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Remark_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 820, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Remark = Remark
Namespace.addCategoryObject('typeBinding', 'Remark', Remark)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Requirement with content type ELEMENT_ONLY
class Requirement (pyxb.binding.basis.complexTypeDefinition):
    """requirement of a part of the use case"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Requirement')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 827, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Requirement_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 832, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Requirement_identifier', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 837, 0), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'identification used in references')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Requirement_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 842, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Requirement_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 847, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __description.name() : __description,
        __identifier.name() : __identifier,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Requirement = Requirement
Namespace.addCategoryObject('typeBinding', 'Requirement', Requirement)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}RequirementCategory with content type ELEMENT_ONLY
class RequirementCategory (pyxb.binding.basis.complexTypeDefinition):
    """Requirements can be sorted in categories. For complex categories the category
name can be "dot-delimited"."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequirementCategory')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 854, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementCategory_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 860, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementCategory_identifier', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 865, 0), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'identification used in references')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementCategory_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 870, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementCategory_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 874, 14), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element Requirement uses Python identifier Requirement
    __Requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Requirement'), 'Requirement', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementCategory_Requirement', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 879, 0), )

    
    Requirement = property(__Requirement.value, __Requirement.set, None, 'information about the requirement')

    _ElementMap.update({
        __description.name() : __description,
        __identifier.name() : __identifier,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __Requirement.name() : __Requirement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RequirementCategory = RequirementCategory
Namespace.addCategoryObject('typeBinding', 'RequirementCategory', RequirementCategory)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}RequirementLibrary with content type ELEMENT_ONLY
class RequirementLibrary (pyxb.binding.basis.complexTypeDefinition):
    """requirements of the repository"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequirementLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 887, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 892, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element RequirementCategory uses Python identifier RequirementCategory
    __RequirementCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RequirementCategory'), 'RequirementCategory', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_RequirementLibrary_RequirementCategory', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 897, 0), )

    
    RequirementCategory = property(__RequirementCategory.value, __RequirementCategory.set, None, 'the category for the requirement')

    _ElementMap.update({
        __name.name() : __name,
        __RequirementCategory.name() : __RequirementCategory
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RequirementLibrary = RequirementLibrary
Namespace.addCategoryObject('typeBinding', 'RequirementLibrary', RequirementLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Scenario with content type ELEMENT_ONLY
class Scenario (pyxb.binding.basis.complexTypeDefinition):
    """a possible sequence of interactions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Scenario')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 904, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Activity uses Python identifier Activity
    __Activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Activity'), 'Activity', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_Activity', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 909, 0), )

    
    Activity = property(__Activity.value, __Activity.set, None, 'list of activities for the scenario')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 914, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element Drawing uses Python identifier Drawing
    __Drawing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Drawing'), 'Drawing', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_Drawing', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 919, 0), )

    
    Drawing = property(__Drawing.value, __Drawing.set, None, 'the list of associated drawing')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 924, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 929, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_number', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 934, 0), )

    
    number = property(__number.value, __number.set, None, 'index of the scenario')

    
    # Element Precondition uses Python identifier Precondition
    __Precondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Precondition'), 'Precondition', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_Precondition', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 939, 0), )

    
    Precondition = property(__Precondition.value, __Precondition.set, None, 'It describes which condition(s) should have been met before this\nscenario happens.')

    
    # Element Postcondition uses Python identifier Postcondition
    __Postcondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Postcondition'), 'Postcondition', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_Postcondition', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 945, 0), )

    
    Postcondition = property(__Postcondition.value, __Postcondition.set, None, 'It describes which condition(s) should prevail after this scenario\nhappens. The post conditions may also define "success" or "failure" conditions for each use case. ')

    
    # Element PrimaryActor uses Python identifier PrimaryActor
    __PrimaryActor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PrimaryActor'), 'PrimaryActor', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_PrimaryActor', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 950, 0), )

    
    PrimaryActor = property(__PrimaryActor.value, __PrimaryActor.set, None, 'It describes which actor triggers this\nscenario.')

    
    # Element Requirement uses Python identifier Requirement
    __Requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Requirement'), 'Requirement', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_Requirement', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 956, 0), )

    
    Requirement = property(__Requirement.value, __Requirement.set, None, 'information about the requirement')

    
    # Element TriggeringEvent uses Python identifier TriggeringEvent
    __TriggeringEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TriggeringEvent'), 'TriggeringEvent', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Scenario_TriggeringEvent', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 961, 0), )

    
    TriggeringEvent = property(__TriggeringEvent.value, __TriggeringEvent.set, None, 'list of triggering events for the scenario')

    _ElementMap.update({
        __Activity.name() : __Activity,
        __description.name() : __description,
        __Drawing.name() : __Drawing,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __number.name() : __number,
        __Precondition.name() : __Precondition,
        __Postcondition.name() : __Postcondition,
        __PrimaryActor.name() : __PrimaryActor,
        __Requirement.name() : __Requirement,
        __TriggeringEvent.name() : __TriggeringEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Scenario = Scenario
Namespace.addCategoryObject('typeBinding', 'Scenario', Scenario)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}TriggeringEvent with content type ELEMENT_ONLY
class TriggeringEvent (pyxb.binding.basis.complexTypeDefinition):
    """It describes which event triggers a scenario."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TriggeringEvent')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 968, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_TriggeringEvent_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 973, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_TriggeringEvent_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 978, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_TriggeringEvent_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 983, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TriggeringEvent = TriggeringEvent
Namespace.addCategoryObject('typeBinding', 'TriggeringEvent', TriggeringEvent)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}UseCase with content type ELEMENT_ONLY
class UseCase (pyxb.binding.basis.complexTypeDefinition):
    """specification of a set of actions performed by a system, which yields an
observable result that is, typically, of value for one or more actors or other stakeholders of the system """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseCase')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 990, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ActorGrouping uses Python identifier ActorGrouping
    __ActorGrouping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ActorGrouping'), 'ActorGrouping', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_ActorGrouping', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 996, 0), )

    
    ActorGrouping = property(__ActorGrouping.value, __ActorGrouping.set, None, 'A use case references several sets of\nactors.')

    
    # Element Assumption uses Python identifier Assumption
    __Assumption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Assumption'), 'Assumption', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Assumption', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1002, 0), )

    
    Assumption = property(__Assumption.value, __Assumption.set, None, 'set of assumptions related to the use case')

    
    # Element BusinessCase uses Python identifier BusinessCase
    __BusinessCase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BusinessCase'), 'BusinessCase', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_BusinessCase', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1007, 0), )

    
    BusinessCase = property(__BusinessCase.value, __BusinessCase.set, None, 'list of business cases associated with the use\ncase')

    
    # Element classification uses Python identifier classification
    __classification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'classification'), 'classification', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_classification', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1013, 0), )

    
    classification = property(__classification.value, __classification.set, None, 'At the international level the use case description might be\ngeneric enough to describe a use case in a more general way independently from the national or regional market design. But\nuse cases might be used to describe regional or national specific circumstances like laws or even project specific details. If the\nuse case reflects those circumstances, it should be characterized accordingly.')

    
    # Element CommonTerm uses Python identifier CommonTerm
    __CommonTerm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CommonTerm'), 'CommonTerm', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_CommonTerm', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1021, 0), )

    
    CommonTerm = property(__CommonTerm.value, __CommonTerm.set, None, 'the associated common terms')

    
    # Element CustomInformation uses Python identifier CustomInformation
    __CustomInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CustomInformation'), 'CustomInformation', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_CustomInformation', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1026, 0), )

    
    CustomInformation = property(__CustomInformation.value, __CustomInformation.set, None, 'related additional information')

    
    # Element Drawing uses Python identifier Drawing
    __Drawing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Drawing'), 'Drawing', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Drawing', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1031, 0), )

    
    Drawing = property(__Drawing.value, __Drawing.set, None, 'the list of associated drawings')

    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_identifier', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1036, 0), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'The identification number (ID) of a use case is unique within a\nrepository or project and serves for organization/administration of use cases.')

    
    # Element KeyPerformanceIndicator uses Python identifier KeyPerformanceIndicator
    __KeyPerformanceIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'KeyPerformanceIndicator'), 'KeyPerformanceIndicator', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_KeyPerformanceIndicator', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1042, 0), )

    
    KeyPerformanceIndicator = property(__KeyPerformanceIndicator.value, __KeyPerformanceIndicator.set, None, 'information about the KPI related to the use\ncase')

    
    # Element keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keywords'), 'keywords', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_keywords', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1048, 0), )

    
    keywords = property(__keywords.value, __keywords.set, None, 'Keywords can be defined in order to support extended search\nfunctionalities within a use case repository. Multiple keywords should be provided as a comma-separated\nlist.')

    
    # Element levelOfDepth uses Python identifier levelOfDepth
    __levelOfDepth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'levelOfDepth'), 'levelOfDepth', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_levelOfDepth', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1055, 0), )

    
    levelOfDepth = property(__levelOfDepth.value, __levelOfDepth.set, None, 'Use cases can be described on different\nlevels.')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1061, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1066, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element Narrative uses Python identifier Narrative
    __Narrative = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Narrative'), 'Narrative', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Narrative', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1071, 0), )

    
    Narrative = property(__Narrative.value, __Narrative.set, None, 'the information about the narrative part of the use\ncase')

    
    # Element nature uses Python identifier nature
    __nature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nature'), 'nature', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_nature', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1077, 0), )

    
    nature = property(__nature.value, __nature.set, None, 'It classifies the main focus of the use case.')

    
    # Element Prerequisite uses Python identifier Prerequisite
    __Prerequisite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Prerequisite'), 'Prerequisite', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Prerequisite', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1082, 0), )

    
    Prerequisite = property(__Prerequisite.value, __Prerequisite.set, None, 'It describes what condition(s) should have been met before\ninitiation of the use case, such as prior state of the actors and activities.')

    
    # Element PrimaryActor uses Python identifier PrimaryActor
    __PrimaryActor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PrimaryActor'), 'PrimaryActor', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_PrimaryActor', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1088, 0), )

    
    PrimaryActor = property(__PrimaryActor.value, __PrimaryActor.set, None, 'identification of the PrimaryActor linked to the use\ncase')

    
    # Element prioritization uses Python identifier prioritization
    __prioritization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'prioritization'), 'prioritization', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_prioritization', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1094, 0), )

    
    prioritization = property(__prioritization.value, __prioritization.set, None, 'If considering a larger number of use cases, it might be\ninteresting to cluster them according to priority.\nThis prioritization might be different from country to country.')

    
    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Reference'), 'Reference', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Reference', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1100, 0), )

    
    Reference = property(__Reference.value, __Reference.set, None, 'information about referenced documents')

    
    # Element RelatedObjective uses Python identifier RelatedObjective
    __RelatedObjective = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RelatedObjective'), 'RelatedObjective', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_RelatedObjective', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1105, 0), )

    
    RelatedObjective = property(__RelatedObjective.value, __RelatedObjective.set, None, 'list of objectives of the use case')

    
    # Element RelatedUseCase uses Python identifier RelatedUseCase
    __RelatedUseCase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RelatedUseCase'), 'RelatedUseCase', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_RelatedUseCase', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1110, 0), )

    
    RelatedUseCase = property(__RelatedUseCase.value, __RelatedUseCase.set, None, 'Known relations to other use cases can be provided here if, for\nexample, the use case is a more detailed one related to a high level use case, or it is an alternative to an existing use\ncase.')

    
    # Element Remark uses Python identifier Remark
    __Remark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Remark'), 'Remark', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Remark', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1117, 0), )

    
    Remark = property(__Remark.value, __Remark.set, None, 'remark associated with the use case')

    
    # Element Scenario uses Python identifier Scenario
    __Scenario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Scenario'), 'Scenario', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Scenario', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1122, 0), )

    
    Scenario = property(__Scenario.value, __Scenario.set, None, 'reference to the scenarios belonging to the use\ncase')

    
    # Element scope uses Python identifier scope
    __scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scope'), 'scope', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_scope', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1128, 0), )

    
    scope = property(__scope.value, __scope.set, None, 'The scope defines the limits of the use\ncase.')

    
    # Element Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCase_Version', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1134, 0), )

    
    Version = property(__Version.value, __Version.set, None, 'list of versions describing changes about the use\ncase')

    _ElementMap.update({
        __ActorGrouping.name() : __ActorGrouping,
        __Assumption.name() : __Assumption,
        __BusinessCase.name() : __BusinessCase,
        __classification.name() : __classification,
        __CommonTerm.name() : __CommonTerm,
        __CustomInformation.name() : __CustomInformation,
        __Drawing.name() : __Drawing,
        __identifier.name() : __identifier,
        __KeyPerformanceIndicator.name() : __KeyPerformanceIndicator,
        __keywords.name() : __keywords,
        __levelOfDepth.name() : __levelOfDepth,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __Narrative.name() : __Narrative,
        __nature.name() : __nature,
        __Prerequisite.name() : __Prerequisite,
        __PrimaryActor.name() : __PrimaryActor,
        __prioritization.name() : __prioritization,
        __Reference.name() : __Reference,
        __RelatedObjective.name() : __RelatedObjective,
        __RelatedUseCase.name() : __RelatedUseCase,
        __Remark.name() : __Remark,
        __Scenario.name() : __Scenario,
        __scope.name() : __scope,
        __Version.name() : __Version
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UseCase = UseCase
Namespace.addCategoryObject('typeBinding', 'UseCase', UseCase)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Version with content type ELEMENT_ONLY
class Version (pyxb.binding.basis.complexTypeDefinition):
    """version of the use case description"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Version')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1142, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element approvalStatus uses Python identifier approvalStatus
    __approvalStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'approvalStatus'), 'approvalStatus', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Version_approvalStatus', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1147, 0), )

    
    approvalStatus = property(__approvalStatus.value, __approvalStatus.set, None, 'information used within the standardization\nprocess')

    
    # Element Author uses Python identifier Author
    __Author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Author'), 'Author', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Version_Author', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1153, 0), )

    
    Author = property(__Author.value, __Author.set, None, 'list of authors participating in the changes of this\nversion')

    
    # Element changes uses Python identifier changes
    __changes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'changes'), 'changes', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Version_changes', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1159, 0), )

    
    changes = property(__changes.value, __changes.set, None, 'It represents the differences with respect to the previous version.\nMultiple changes are separated with paragraphs.')

    
    # Element date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Version_date', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1165, 0), )

    
    date = property(__date.value, __date.set, None, 'date of creation of the version, in the format YYYY-MMDD')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Version_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1169, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Version_number', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1174, 0), )

    
    number = property(__number.value, __number.set, None, 'sequential number to identify the version of the\ndocument')

    _ElementMap.update({
        __approvalStatus.name() : __approvalStatus,
        __Author.name() : __Author,
        __changes.name() : __changes,
        __date.name() : __date,
        __mRID.name() : __mRID,
        __number.name() : __number
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Version = Version
Namespace.addCategoryObject('typeBinding', 'Version', Version)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}UseCaseLibrary with content type ELEMENT_ONLY
class UseCaseLibrary (pyxb.binding.basis.complexTypeDefinition):
    """use cases of the repository"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseCaseLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1182, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1187, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element UseCase uses Python identifier UseCase
    __UseCase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UseCase'), 'UseCase', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseLibrary_UseCase', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1192, 0), )

    
    UseCase = property(__UseCase.value, __UseCase.set, None, 'list of use cases within the library')

    _ElementMap.update({
        __name.name() : __name,
        __UseCase.name() : __UseCase
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UseCaseLibrary = UseCaseLibrary
Namespace.addCategoryObject('typeBinding', 'UseCaseLibrary', UseCaseLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}UseCaseRepository_Type with content type ELEMENT_ONLY
class UseCaseRepository_Type (pyxb.binding.basis.complexTypeDefinition):
    """database, based on a given use cases template, for editing, maintenance and
administration of use cases, actors and requirements including their interrelations"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseCaseRepository_Type')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1199, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ActorLibrary uses Python identifier ActorLibrary
    __ActorLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ActorLibrary'), 'ActorLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_ActorLibrary', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1205, 0), )

    
    ActorLibrary = property(__ActorLibrary.value, __ActorLibrary.set, None, 'library of actors')

    
    # Element AreaLibrary uses Python identifier AreaLibrary
    __AreaLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AreaLibrary'), 'AreaLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_AreaLibrary', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1210, 0), )

    
    AreaLibrary = property(__AreaLibrary.value, __AreaLibrary.set, None, 'the associated library of areas')

    
    # Element BusinessCaseLibrary uses Python identifier BusinessCaseLibrary
    __BusinessCaseLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BusinessCaseLibrary'), 'BusinessCaseLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_BusinessCaseLibrary', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1215, 0), )

    
    BusinessCaseLibrary = property(__BusinessCaseLibrary.value, __BusinessCaseLibrary.set, None, 'the library associated with the repository')

    
    # Element BusinessObjectLibrary uses Python identifier BusinessObjectLibrary
    __BusinessObjectLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BusinessObjectLibrary'), 'BusinessObjectLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_BusinessObjectLibrary', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1220, 0), )

    
    BusinessObjectLibrary = property(__BusinessObjectLibrary.value, __BusinessObjectLibrary.set, None, 'the library of business objects')

    
    # Element CommonTermLibrary uses Python identifier CommonTermLibrary
    __CommonTermLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CommonTermLibrary'), 'CommonTermLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_CommonTermLibrary', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1225, 0), )

    
    CommonTermLibrary = property(__CommonTermLibrary.value, __CommonTermLibrary.set, None, 'the associated library of common terms')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1230, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1235, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1240, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element RequirementLibrary uses Python identifier RequirementLibrary
    __RequirementLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RequirementLibrary'), 'RequirementLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_RequirementLibrary', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1244, 0), )

    
    RequirementLibrary = property(__RequirementLibrary.value, __RequirementLibrary.set, None, 'the associated library')

    
    # Element UseCaseLibrary uses Python identifier UseCaseLibrary
    __UseCaseLibrary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UseCaseLibrary'), 'UseCaseLibrary', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_UseCaseRepository_Type_UseCaseLibrary', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1249, 0), )

    
    UseCaseLibrary = property(__UseCaseLibrary.value, __UseCaseLibrary.set, None, 'the associated library of use cases')

    _ElementMap.update({
        __ActorLibrary.name() : __ActorLibrary,
        __AreaLibrary.name() : __AreaLibrary,
        __BusinessCaseLibrary.name() : __BusinessCaseLibrary,
        __BusinessObjectLibrary.name() : __BusinessObjectLibrary,
        __CommonTermLibrary.name() : __CommonTermLibrary,
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __RequirementLibrary.name() : __RequirementLibrary,
        __UseCaseLibrary.name() : __UseCaseLibrary
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UseCaseRepository_Type = UseCaseRepository_Type
Namespace.addCategoryObject('typeBinding', 'UseCaseRepository_Type', UseCaseRepository_Type)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}AreaLibrary with content type ELEMENT_ONLY
class AreaLibrary (pyxb.binding.basis.complexTypeDefinition):
    """areas of the repository"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AreaLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1257, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Area uses Python identifier Area
    __Area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Area'), 'Area', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_AreaLibrary_Area', True, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1262, 0), )

    
    Area = property(__Area.value, __Area.set, None, 'the list of areas within the library')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_AreaLibrary_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1267, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    _ElementMap.update({
        __Area.name() : __Area,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AreaLibrary = AreaLibrary
Namespace.addCategoryObject('typeBinding', 'AreaLibrary', AreaLibrary)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Assumption with content type ELEMENT_ONLY
class Assumption (pyxb.binding.basis.complexTypeDefinition):
    """It may be used to define a further general assumption for a use case, such as
which systems already exist, which contractual relations exist, and which configurations of systems are probably in place. Initial
states of information exchanged shall also be identified."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Assumption')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1274, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Assumption_description', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1281, 0), )

    
    description = property(__description.value, __description.set, None, 'description of the object')

    
    # Element mRID uses Python identifier mRID
    __mRID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mRID'), 'mRID', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Assumption_mRID', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1286, 0), )

    
    mRID = property(__mRID.value, __mRID.set, None, 'master resource identifier')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Assumption_name', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1291, 0), )

    
    name = property(__name.value, __name.set, None, 'a short name')

    
    # Element number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Assumption_number', False, pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1296, 0), )

    
    number = property(__number.value, __number.set, None, 'index of the assumption')

    _ElementMap.update({
        __description.name() : __description,
        __mRID.name() : __mRID,
        __name.name() : __name,
        __number.name() : __number
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Assumption = Assumption
Namespace.addCategoryObject('typeBinding', 'Assumption', Assumption)


# Complex type {http://www.SYC.org/IEC62559/part3/UC/V01/Build08082016}Resource_String with content type SIMPLE
class Resource_String (pyxb.binding.basis.complexTypeDefinition):
    """String Primitive type"""
    _TypeDefinition = Resource_String_value_ValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Resource_String')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 203, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is Resource_String_value_ValueType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_SYC_orgIEC62559part3UCV01Build08082016_Resource_String_type', _module_typeBindings.ResourceType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 209, 0)
    __type._UseLocation = pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 209, 0)
    
    type = property(__type.value, __type.set, None, 'supplementary attribute of the data\ntype')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.Resource_String = Resource_String
Namespace.addCategoryObject('typeBinding', 'Resource_String', Resource_String)


UseCaseRepository = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UseCaseRepository'), UseCaseRepository_Type, location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1256, 0))
Namespace.addCategoryObject('elementBinding', UseCaseRepository.name().localName(), UseCaseRepository)



Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BusinessObject'), Ref_BusinessObject, scope=Activity, documentation='This describes briefly the information to be exchanged between\nthe two actors – information producer and information receiver. It may list several information items in one step, comma\nseparated.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 11, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ChildActivity'), Activity, scope=Activity, documentation='child activities', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 19, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Activity, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 24, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Drawing'), Drawing, scope=Activity, documentation='the list of associated drawing', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 29, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event'), pyxb.binding.datatypes.string, scope=Activity, documentation='It is the event that triggers the step. This might be completion of\nprevious steps (in that case the event is the comma-separated list of their numbers) or the condition to exit a\nloop.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 34, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InformationProducer'), Ref_Actor, scope=Activity, documentation='This identifies the producer or source of the information. Thisshould be one of the actors defined in the repository.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 41, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InformationReceiver'), Ref_Actor, scope=Activity, documentation='This identifies the receiver of the information. This should be one\nof the actors defined in the repository.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 47, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Activity, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 54, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Activity, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 59, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number'), pyxb.binding.datatypes.string, scope=Activity, documentation='index of the activity', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 64, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PrimaryActor'), Ref_Actor, scope=Activity, documentation='reference to the PrimaryActor', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 69, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Requirement'), Ref_Requirement, scope=Activity, documentation='Several requirements may be listed in one step, comma\nseparated.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 74, 0)))

Activity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'service'), pyxb.binding.datatypes.string, scope=Activity, documentation='This column identifies the nature of the information flow and the\noriginator of the information. Available options are CREATE, GET, CHANGE, DELETE, CANCEL, EXECUTE derived from\nIEC 61968-100:2013.\nAdditionally, REPORT, TIMER and REPEAT are suggested.\n- CREATE means that an information object is to be created at the Producer.\n- GET (this is the default value if none is populated) means that the Receiver requests information from the Producer\n(default).\n- CHANGE means that information is to be updated. Producer updates the Receiver’s information.\n- DELETE means that information is to be deleted. Producer deletes information from the Receiver.\n- CANCEL, CLOSE imply actions related to processes, such as the closure of a work order or the cancellation of a\ncontrol request.\n- EXECUTE is used when a complex transaction is being conveyed using a service, which potentially contains more\nthan one verb.\n- REPORT is used to represent transferral of unsolicited information or asynchronous information flows. Producer\nprovides information to the Receiver.\n- TIMER is used to represent a waiting period. When using the TIMER service, the Information Producer and\nInformation Receiver fields shall refer to the same actor.\n- REPEAT is used to indicate that a series of steps is repeated until a condition or trigger event. The condition is\nspecified as the text in the "Event" column for this row or step. Following the word REPEAT, the first and last step numbers of\nthe series to be repeated shall appear, in parenthesis, in the following form: REPEAT(X-Y) where X is the first step and Y is the\nlast step.\nThese common service definitions are related to automation/information or communication systems. In case the use case\ntemplate is applied in other domains, further services might be used and described.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 81, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 11, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 19, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 29, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 34, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 41, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 47, 0))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 54, 0))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 64, 0))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 69, 0))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 74, 0))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 81, 0))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'BusinessObject')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 11, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'ChildActivity')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 19, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 24, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'Drawing')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 29, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'event')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 34, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'InformationProducer')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 41, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'InformationReceiver')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 47, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 54, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 59, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'number')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 64, 0))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'PrimaryActor')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 69, 0))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'Requirement')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 74, 0))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Activity._UseForTag(pyxb.namespace.ExpandedName(None, 'service')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 81, 0))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Activity._Automaton = _BuildAutomaton()




Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'drawingType'), DrawingClassification, scope=Drawing, documentation='type of drawing', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 117, 0)))

Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Drawing, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 121, 0)))

Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Drawing, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 126, 0)))

Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URI'), Resource_String, scope=Drawing, documentation='resource Path to an image file\nex: http://www..../image.jpg\nor\npath to an XMI file with a relative diagram path from the root of the UML model. ex:\nhttp://www.../Model.xmi#Package1/Package2/.../DiagName', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 131, 0)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 121, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Drawing._UseForTag(pyxb.namespace.ExpandedName(None, 'drawingType')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 117, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Drawing._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 121, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Drawing._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 126, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Drawing._UseForTag(pyxb.namespace.ExpandedName(None, 'URI')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 131, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Drawing._Automaton = _BuildAutomaton_()




Ref_Requirement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_Requirement, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 243, 0)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_Requirement._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 243, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_Requirement._Automaton = _BuildAutomaton_2()




Ref_Actor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_Actor, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 257, 0)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_Actor._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 257, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_Actor._Automaton = _BuildAutomaton_3()




Ref_BusinessObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_BusinessObject, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 269, 0)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_BusinessObject._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 269, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_BusinessObject._Automaton = _BuildAutomaton_4()




Actor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Actor, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 282, 0)))

Actor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Actor, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 287, 0)))

Actor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Actor, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 292, 0)))

Actor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=Actor, documentation='type of the actor (business, system, ...)', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 297, 0)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 282, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 287, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 297, 0))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Actor._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 282, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Actor._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 287, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Actor._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 292, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Actor._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 297, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Actor._Automaton = _BuildAutomaton_5()




ActorGrouping._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ActorGrouping, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 309, 0)))

ActorGrouping._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FurtherActorInformation'), FurtherActorInformation, scope=ActorGrouping, documentation='In a context of one use case, an actor grouped into an\nActorGrouping may have one FurtherActorInformation.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 314, 0)))

ActorGrouping._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=ActorGrouping, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 321, 0)))

ActorGrouping._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=ActorGrouping, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 326, 0)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 309, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 314, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 321, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 326, 0))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActorGrouping._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 309, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ActorGrouping._UseForTag(pyxb.namespace.ExpandedName(None, 'FurtherActorInformation')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 314, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ActorGrouping._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 321, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ActorGrouping._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 326, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ActorGrouping._Automaton = _BuildAutomaton_6()




FurtherActorInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Actor'), Ref_Actor, scope=FurtherActorInformation, documentation='information related to an actor', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 339, 0)))

FurtherActorInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=FurtherActorInformation, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 344, 0)))

FurtherActorInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=FurtherActorInformation, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 348, 0)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 339, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 344, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 348, 0))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FurtherActorInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'Actor')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 339, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FurtherActorInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 344, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FurtherActorInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 348, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FurtherActorInformation._Automaton = _BuildAutomaton_7()




ActorLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Actor'), Actor, scope=ActorLibrary, documentation='the actors listed in the library', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 360, 0)))

ActorLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=ActorLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 365, 0)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 360, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 365, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActorLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'Actor')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 360, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ActorLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 365, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ActorLibrary._Automaton = _BuildAutomaton_8()




Area._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Area, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 378, 0)))

Area._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Area, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 383, 0)))

Area._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Area, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 388, 0)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 378, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 383, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Area._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 378, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Area._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 383, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Area._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 388, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Area._Automaton = _BuildAutomaton_9()




Author._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Author, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 402, 0)))

Author._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Author, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 407, 0)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 402, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 407, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Author._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 402, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Author._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 407, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Author._Automaton = _BuildAutomaton_10()




BusinessCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Area'), Ref_Area, scope=BusinessCase, documentation='Use cases can be used in various areas (e.g. energy system).Within these areas different domains are used to define / determine a more specific subgrouping. One or more domains and\nzones, comma separated, can be specified in the template.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 420, 0)))

BusinessCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=BusinessCase, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 426, 0)))

BusinessCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=BusinessCase, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 431, 0)))

BusinessCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=BusinessCase, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 436, 0)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 420, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 426, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 431, 0))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BusinessCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Area')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 420, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BusinessCase._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 426, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BusinessCase._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 431, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BusinessCase._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 436, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BusinessCase._Automaton = _BuildAutomaton_11()




Ref_Area._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_Area, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 449, 0)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_Area._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 449, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_Area._Automaton = _BuildAutomaton_12()




BusinessCaseLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BusinessCase'), BusinessCase, scope=BusinessCaseLibrary, documentation='the list of business cases', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 461, 0)))

BusinessCaseLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=BusinessCaseLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 466, 0)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 461, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 466, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BusinessCaseLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'BusinessCase')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 461, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BusinessCaseLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 466, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BusinessCaseLibrary._Automaton = _BuildAutomaton_13()




BusinessObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=BusinessObject, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 478, 0)))

BusinessObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=BusinessObject, documentation='identification used in references in the use case\ndescription', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 483, 0)))

BusinessObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=BusinessObject, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 489, 0)))

BusinessObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=BusinessObject, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 494, 0)))

BusinessObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Requirement'), Ref_Requirement, scope=BusinessObject, documentation='It can be used to define requirements related to the information\nand not to the step as in the step by step analysis.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 498, 0)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 478, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 489, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 498, 0))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BusinessObject._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 478, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BusinessObject._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 483, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BusinessObject._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 489, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BusinessObject._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 494, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BusinessObject._UseForTag(pyxb.namespace.ExpandedName(None, 'Requirement')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 498, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BusinessObject._Automaton = _BuildAutomaton_14()




BusinessObjectLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BusinessObject'), BusinessObject, scope=BusinessObjectLibrary, documentation='list of business objects within the library', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 511, 0)))

BusinessObjectLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=BusinessObjectLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 516, 0)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 511, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 516, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BusinessObjectLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'BusinessObject')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 511, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BusinessObjectLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 516, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BusinessObjectLibrary._Automaton = _BuildAutomaton_15()




CommonTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CommonTerm, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 528, 0)))

CommonTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=CommonTerm, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 533, 0)))

CommonTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CommonTerm, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 538, 0)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 528, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 533, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 538, 0))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommonTerm._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 528, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CommonTerm._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 533, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CommonTerm._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 538, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CommonTerm._Automaton = _BuildAutomaton_16()




CommonTermLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CommonTerm'), CommonTerm, scope=CommonTermLibrary, documentation='list of common terms', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 550, 0)))

CommonTermLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CommonTermLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 555, 0)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 550, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 555, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommonTermLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'CommonTerm')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 550, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CommonTermLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 555, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CommonTermLibrary._Automaton = _BuildAutomaton_17()




Condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Condition, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 567, 0)))

Condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Condition, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 571, 0)))

Condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Condition, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 576, 0)))

Condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number'), pyxb.binding.datatypes.string, scope=Condition, documentation='index of the condition', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 581, 0)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 567, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 571, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 576, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 581, 0))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Condition._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 567, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Condition._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 571, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Condition._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 576, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Condition._UseForTag(pyxb.namespace.ExpandedName(None, 'number')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 581, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Condition._Automaton = _BuildAutomaton_18()




CustomInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'key'), pyxb.binding.datatypes.string, scope=CustomInformation, documentation='unique key for identification purposes', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 594, 0)))

CustomInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=CustomInformation, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 599, 0)))

CustomInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reference'), pyxb.binding.datatypes.string, scope=CustomInformation, documentation='This field refers to relevant template\nsection.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 604, 0)))

CustomInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.string, scope=CustomInformation, documentation='the corresponding information for the provided\nkey', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 610, 0)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 594, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 599, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 604, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 610, 0))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CustomInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'key')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 594, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CustomInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 599, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CustomInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'reference')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 604, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CustomInformation._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 610, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CustomInformation._Automaton = _BuildAutomaton_19()




KeyPerformanceIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=KeyPerformanceIndicator, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 624, 0)))

KeyPerformanceIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=KeyPerformanceIndicator, documentation='unique identifier for the Key Performance Indicator\n(KPI)', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 629, 0)))

KeyPerformanceIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=KeyPerformanceIndicator, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 635, 0)))

KeyPerformanceIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=KeyPerformanceIndicator, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 640, 0)))

KeyPerformanceIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Objective'), Ref_Objective, scope=KeyPerformanceIndicator, documentation='the related objective', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 645, 0)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 624, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 629, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 635, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 640, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 645, 0))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(KeyPerformanceIndicator._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 624, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(KeyPerformanceIndicator._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 629, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(KeyPerformanceIndicator._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 635, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(KeyPerformanceIndicator._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 640, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(KeyPerformanceIndicator._UseForTag(pyxb.namespace.ExpandedName(None, 'Objective')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 645, 0))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
KeyPerformanceIndicator._Automaton = _BuildAutomaton_20()




Ref_Objective._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_Objective, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 656, 0)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_Objective._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 656, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_Objective._Automaton = _BuildAutomaton_21()




Narrative._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'completeDescription'), pyxb.binding.datatypes.string, scope=Narrative, documentation='It provides a complete narrative of the use case from a user’s\npoint of view, describing what occurs when, why, with what expectation, and under what conditions. This narrative should be\nwritten in plain text so that non-domain experts can understand it.\nThe length of the complete description can range from a few sentences to a few pages, depending on the complexity and/or\nnewness of the use case. This description often helps the domain expert to reflect on the requirements for the use case before\ngetting into the details in the next sections of the use case template.\nThe description may include drawings for explanation.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 668, 0)))

Narrative._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Narrative, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 679, 0)))

Narrative._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shortDescription'), pyxb.binding.datatypes.string, scope=Narrative, documentation='It is a short text intended to summarize the main idea as a\nservice for the reader who is searching for a use case or looking for an overview.\nRecommendation: This short description should have not more than 150 words.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 684, 0)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 668, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 679, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Narrative._UseForTag(pyxb.namespace.ExpandedName(None, 'completeDescription')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 668, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Narrative._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 679, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Narrative._UseForTag(pyxb.namespace.ExpandedName(None, 'shortDescription')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 684, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Narrative._Automaton = _BuildAutomaton_22()




Objective._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Objective, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 698, 0)))

Objective._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Objective, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 703, 0)))

Objective._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Objective, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 708, 0)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 698, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 703, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Objective._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 698, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Objective._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 703, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Objective._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 708, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Objective._Automaton = _BuildAutomaton_23()




Ref_BusinessCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_BusinessCase, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 721, 0)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_BusinessCase._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 721, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_BusinessCase._Automaton = _BuildAutomaton_24()




Ref_CommonTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_CommonTerm, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 732, 0)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_CommonTerm._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 732, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_CommonTerm._Automaton = _BuildAutomaton_25()




Ref_UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Ref_UseCase, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 745, 0)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Ref_UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 745, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Ref_UseCase._Automaton = _BuildAutomaton_26()




Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Reference, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 759, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'impact'), pyxb.binding.datatypes.string, scope=Reference, documentation='This information describes the nature of the influence of the\ndocument on the use case.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 764, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'link'), pyxb.binding.datatypes.string, scope=Reference, documentation='If available, a public link to the document can be\nprovided.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 770, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Reference, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 776, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Reference, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 781, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number'), pyxb.binding.datatypes.string, scope=Reference, documentation='index of the reference', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 786, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'originatorOrganization'), pyxb.binding.datatypes.string, scope=Reference, documentation='This describes the name of the organization publishing the\ndocument.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 791, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'status'), pyxb.binding.datatypes.string, scope=Reference, documentation='status of the referenced document', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 797, 0)))

Reference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=Reference, documentation='There are different reference types (e.g. standard, regulation,\ncontract, others like publications).', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 801, 0)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 759, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 764, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 770, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 776, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 786, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 797, 0))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 801, 0))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 759, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'impact')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 764, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'link')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 770, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 776, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 781, 0))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'number')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 786, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'originatorOrganization')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 791, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'status')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 797, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 801, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Reference._Automaton = _BuildAutomaton_27()




Remark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Remark, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 815, 0)))

Remark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Remark, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 820, 0)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 815, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 820, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Remark._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 815, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Remark._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 820, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Remark._Automaton = _BuildAutomaton_28()




Requirement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Requirement, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 832, 0)))

Requirement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=Requirement, documentation='identification used in references', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 837, 0)))

Requirement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Requirement, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 842, 0)))

Requirement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Requirement, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 847, 0)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 832, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 837, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 842, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 847, 0))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Requirement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 832, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Requirement._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 837, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Requirement._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 842, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Requirement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 847, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Requirement._Automaton = _BuildAutomaton_29()




RequirementCategory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=RequirementCategory, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 860, 0)))

RequirementCategory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=RequirementCategory, documentation='identification used in references', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 865, 0)))

RequirementCategory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=RequirementCategory, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 870, 0)))

RequirementCategory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=RequirementCategory, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 874, 14)))

RequirementCategory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Requirement'), Requirement, scope=RequirementCategory, documentation='information about the requirement', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 879, 0)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 860, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 870, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 879, 0))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequirementCategory._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 860, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequirementCategory._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 865, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequirementCategory._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 870, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RequirementCategory._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 874, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RequirementCategory._UseForTag(pyxb.namespace.ExpandedName(None, 'Requirement')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 879, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RequirementCategory._Automaton = _BuildAutomaton_30()




RequirementLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=RequirementLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 892, 0)))

RequirementLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RequirementCategory'), RequirementCategory, scope=RequirementLibrary, documentation='the category for the requirement', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 897, 0)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 892, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 897, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RequirementLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 892, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RequirementLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'RequirementCategory')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 897, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequirementLibrary._Automaton = _BuildAutomaton_31()




Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Activity'), Activity, scope=Scenario, documentation='list of activities for the scenario', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 909, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Scenario, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 914, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Drawing'), Drawing, scope=Scenario, documentation='the list of associated drawing', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 919, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Scenario, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 924, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Scenario, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 929, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number'), pyxb.binding.datatypes.string, scope=Scenario, documentation='index of the scenario', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 934, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Precondition'), Condition, scope=Scenario, documentation='It describes which condition(s) should have been met before this\nscenario happens.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 939, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Postcondition'), Condition, scope=Scenario, documentation='It describes which condition(s) should prevail after this scenario\nhappens. The post conditions may also define "success" or "failure" conditions for each use case. ', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 945, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PrimaryActor'), Ref_Actor, scope=Scenario, documentation='It describes which actor triggers this\nscenario.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 950, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Requirement'), Ref_Requirement, scope=Scenario, documentation='information about the requirement', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 956, 0)))

Scenario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TriggeringEvent'), TriggeringEvent, scope=Scenario, documentation='list of triggering events for the scenario', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 961, 0)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 909, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 914, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 919, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 924, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 934, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 939, 0))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 945, 0))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 950, 0))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 956, 0))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 961, 0))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'Activity')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 909, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 914, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'Drawing')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 919, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 924, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 929, 0))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'number')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 934, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'Precondition')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 939, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'Postcondition')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 945, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'PrimaryActor')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 950, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'Requirement')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 956, 0))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Scenario._UseForTag(pyxb.namespace.ExpandedName(None, 'TriggeringEvent')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 961, 0))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Scenario._Automaton = _BuildAutomaton_32()




TriggeringEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=TriggeringEvent, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 973, 0)))

TriggeringEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=TriggeringEvent, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 978, 0)))

TriggeringEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=TriggeringEvent, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 983, 0)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 973, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 978, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 983, 0))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TriggeringEvent._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 973, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TriggeringEvent._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 978, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TriggeringEvent._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 983, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TriggeringEvent._Automaton = _BuildAutomaton_33()




UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ActorGrouping'), ActorGrouping, scope=UseCase, documentation='A use case references several sets of\nactors.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 996, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Assumption'), Assumption, scope=UseCase, documentation='set of assumptions related to the use case', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1002, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BusinessCase'), Ref_BusinessCase, scope=UseCase, documentation='list of business cases associated with the use\ncase', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1007, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'classification'), pyxb.binding.datatypes.string, scope=UseCase, documentation='At the international level the use case description might be\ngeneric enough to describe a use case in a more general way independently from the national or regional market design. But\nuse cases might be used to describe regional or national specific circumstances like laws or even project specific details. If the\nuse case reflects those circumstances, it should be characterized accordingly.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1013, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CommonTerm'), Ref_CommonTerm, scope=UseCase, documentation='the associated common terms', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1021, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CustomInformation'), CustomInformation, scope=UseCase, documentation='related additional information', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1026, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Drawing'), Drawing, scope=UseCase, documentation='the list of associated drawings', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1031, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=UseCase, documentation='The identification number (ID) of a use case is unique within a\nrepository or project and serves for organization/administration of use cases.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1036, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'KeyPerformanceIndicator'), KeyPerformanceIndicator, scope=UseCase, documentation='information about the KPI related to the use\ncase', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1042, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keywords'), pyxb.binding.datatypes.string, scope=UseCase, documentation='Keywords can be defined in order to support extended search\nfunctionalities within a use case repository. Multiple keywords should be provided as a comma-separated\nlist.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1048, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'levelOfDepth'), pyxb.binding.datatypes.string, scope=UseCase, documentation='Use cases can be described on different\nlevels.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1055, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=UseCase, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1061, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=UseCase, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1066, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Narrative'), Narrative, scope=UseCase, documentation='the information about the narrative part of the use\ncase', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1071, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nature'), pyxb.binding.datatypes.string, scope=UseCase, documentation='It classifies the main focus of the use case.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1077, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Prerequisite'), Condition, scope=UseCase, documentation='It describes what condition(s) should have been met before\ninitiation of the use case, such as prior state of the actors and activities.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1082, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PrimaryActor'), Ref_Actor, scope=UseCase, documentation='identification of the PrimaryActor linked to the use\ncase', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1088, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'prioritization'), pyxb.binding.datatypes.string, scope=UseCase, documentation='If considering a larger number of use cases, it might be\ninteresting to cluster them according to priority.\nThis prioritization might be different from country to country.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1094, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Reference'), Reference, scope=UseCase, documentation='information about referenced documents', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1100, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RelatedObjective'), Objective, scope=UseCase, documentation='list of objectives of the use case', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1105, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RelatedUseCase'), Ref_UseCase, scope=UseCase, documentation='Known relations to other use cases can be provided here if, for\nexample, the use case is a more detailed one related to a high level use case, or it is an alternative to an existing use\ncase.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1110, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Remark'), Remark, scope=UseCase, documentation='remark associated with the use case', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1117, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Scenario'), Scenario, scope=UseCase, documentation='reference to the scenarios belonging to the use\ncase', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1122, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scope'), pyxb.binding.datatypes.string, scope=UseCase, documentation='The scope defines the limits of the use\ncase.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1128, 0)))

UseCase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Version'), Version, scope=UseCase, documentation='list of versions describing changes about the use\ncase', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1134, 0)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 996, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1002, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1007, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1013, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1021, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1026, 0))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1031, 0))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1042, 0))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1048, 0))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1055, 0))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1061, 0))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1071, 0))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1077, 0))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1082, 0))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1088, 0))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1094, 0))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1100, 0))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1105, 0))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1110, 0))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1117, 0))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1122, 0))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1128, 0))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1134, 0))
    counters.add(cc_22)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'ActorGrouping')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 996, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Assumption')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1002, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'BusinessCase')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1007, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'classification')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1013, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'CommonTerm')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1021, 0))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'CustomInformation')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1026, 0))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Drawing')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1031, 0))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1036, 0))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'KeyPerformanceIndicator')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1042, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'keywords')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1048, 0))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'levelOfDepth')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1055, 0))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1061, 0))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1066, 0))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Narrative')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1071, 0))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'nature')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1077, 0))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Prerequisite')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1082, 0))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'PrimaryActor')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1088, 0))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'prioritization')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1094, 0))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Reference')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1100, 0))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'RelatedObjective')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1105, 0))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'RelatedUseCase')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1110, 0))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Remark')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1117, 0))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Scenario')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1122, 0))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'scope')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1128, 0))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(UseCase._UseForTag(pyxb.namespace.ExpandedName(None, 'Version')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1134, 0))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    st_24._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UseCase._Automaton = _BuildAutomaton_34()




Version._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'approvalStatus'), pyxb.binding.datatypes.string, scope=Version, documentation='information used within the standardization\nprocess', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1147, 0)))

Version._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Author'), Author, scope=Version, documentation='list of authors participating in the changes of this\nversion', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1153, 0)))

Version._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'changes'), pyxb.binding.datatypes.string, scope=Version, documentation='It represents the differences with respect to the previous version.\nMultiple changes are separated with paragraphs.', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1159, 0)))

Version._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'date'), pyxb.binding.datatypes.dateTime, scope=Version, documentation='date of creation of the version, in the format YYYY-MMDD', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1165, 0)))

Version._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Version, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1169, 0)))

Version._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number'), pyxb.binding.datatypes.string, scope=Version, documentation='sequential number to identify the version of the\ndocument', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1174, 0)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1147, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1153, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1159, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1169, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1174, 0))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Version._UseForTag(pyxb.namespace.ExpandedName(None, 'approvalStatus')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1147, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Version._UseForTag(pyxb.namespace.ExpandedName(None, 'Author')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1153, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Version._UseForTag(pyxb.namespace.ExpandedName(None, 'changes')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1159, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Version._UseForTag(pyxb.namespace.ExpandedName(None, 'date')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1165, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Version._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1169, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Version._UseForTag(pyxb.namespace.ExpandedName(None, 'number')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1174, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Version._Automaton = _BuildAutomaton_35()




UseCaseLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=UseCaseLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1187, 0)))

UseCaseLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UseCase'), UseCase, scope=UseCaseLibrary, documentation='list of use cases within the library', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1192, 0)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1187, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1192, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UseCaseLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1187, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UseCaseLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'UseCase')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1192, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UseCaseLibrary._Automaton = _BuildAutomaton_36()




UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ActorLibrary'), ActorLibrary, scope=UseCaseRepository_Type, documentation='library of actors', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1205, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AreaLibrary'), AreaLibrary, scope=UseCaseRepository_Type, documentation='the associated library of areas', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1210, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BusinessCaseLibrary'), BusinessCaseLibrary, scope=UseCaseRepository_Type, documentation='the library associated with the repository', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1215, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BusinessObjectLibrary'), BusinessObjectLibrary, scope=UseCaseRepository_Type, documentation='the library of business objects', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1220, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CommonTermLibrary'), CommonTermLibrary, scope=UseCaseRepository_Type, documentation='the associated library of common terms', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1225, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=UseCaseRepository_Type, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1230, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=UseCaseRepository_Type, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1235, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=UseCaseRepository_Type, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1240, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RequirementLibrary'), RequirementLibrary, scope=UseCaseRepository_Type, documentation='the associated library', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1244, 0)))

UseCaseRepository_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UseCaseLibrary'), UseCaseLibrary, scope=UseCaseRepository_Type, documentation='the associated library of use cases', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1249, 0)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1205, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1210, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1215, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1220, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1225, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1230, 0))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1235, 0))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1244, 0))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1249, 0))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'ActorLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1205, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'AreaLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1210, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'BusinessCaseLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1215, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'BusinessObjectLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1220, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'CommonTermLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1225, 0))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1230, 0))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1235, 0))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1240, 0))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'RequirementLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1244, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UseCaseRepository_Type._UseForTag(pyxb.namespace.ExpandedName(None, 'UseCaseLibrary')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1249, 0))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UseCaseRepository_Type._Automaton = _BuildAutomaton_37()




AreaLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Area'), Area, scope=AreaLibrary, documentation='the list of areas within the library', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1262, 0)))

AreaLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=AreaLibrary, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1267, 0)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1262, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1267, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AreaLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'Area')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1262, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AreaLibrary._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1267, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AreaLibrary._Automaton = _BuildAutomaton_38()




Assumption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Assumption, documentation='description of the object', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1281, 0)))

Assumption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mRID'), pyxb.binding.datatypes.string, scope=Assumption, documentation='master resource identifier', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1286, 0)))

Assumption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Assumption, documentation='a short name', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1291, 0)))

Assumption._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number'), pyxb.binding.datatypes.string, scope=Assumption, documentation='index of the assumption', location=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1296, 0)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1281, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1286, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1291, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1296, 0))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Assumption._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1281, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Assumption._UseForTag(pyxb.namespace.ExpandedName(None, 'mRID')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1286, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Assumption._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1291, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Assumption._UseForTag(pyxb.namespace.ExpandedName(None, 'number')), pyxb.utils.utility.Location('/mnt/c/Users/vlacort/Documents/ETRA/Proyectos/BRIDGE/IEC62559-3.xsd', 1296, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Assumption._Automaton = _BuildAutomaton_39()

