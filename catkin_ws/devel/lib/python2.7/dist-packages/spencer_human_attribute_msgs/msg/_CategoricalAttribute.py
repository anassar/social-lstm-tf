# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from spencer_human_attribute_msgs/CategoricalAttribute.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CategoricalAttribute(genpy.Message):
  _md5sum = "022dc607a1c6f3404ecf625be18f25f5"
  _type = "spencer_human_attribute_msgs/CategoricalAttribute"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint64                  subject_id              # either an observation ID or a track ID (if information has been integrated over time); should be encoded in topic name
string                  type                    # type of the attribute, see constants below

string[]                values                  # values, each value also should have a confidence, highest-confidence attribute should come first
float32[]               confidences             # corresponding confidences should sum up to 1.0, highest confidence comes first


##################################################
### Constants for categorical attribute types. ###
##################################################

string      GENDER        = gender
string      AGE_GROUP     = age_group

###################################################
### Constants for categorical attribute values. ###
###################################################

string      GENDER_MALE             = male
string      GENDER_FEMALE           = female

# Age groups are based upon the categories from the "Images Of Groups" RGB database
string      AGE_GROUP_0_TO_2        = 0-2
string      AGE_GROUP_3_TO_7        = 3-7
string      AGE_GROUP_8_TO_12       = 8-12
string      AGE_GROUP_13_TO_19      = 13-19
string      AGE_GROUP_20_TO_36      = 20-36
string      AGE_GROUP_37_TO_65      = 37-65
string      AGE_GROUP_66_TO_99      = 66-99



"""
  # Pseudo-constants
  GENDER = 'gender'
  AGE_GROUP = 'age_group'
  GENDER_MALE = 'male'
  GENDER_FEMALE = 'female'
  AGE_GROUP_0_TO_2 = '0-2'
  AGE_GROUP_3_TO_7 = '3-7'
  AGE_GROUP_8_TO_12 = '8-12'
  AGE_GROUP_13_TO_19 = '13-19'
  AGE_GROUP_20_TO_36 = '20-36'
  AGE_GROUP_37_TO_65 = '37-65'
  AGE_GROUP_66_TO_99 = '66-99'

  __slots__ = ['subject_id','type','values','confidences']
  _slot_types = ['uint64','string','string[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       subject_id,type,values,confidences

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CategoricalAttribute, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.subject_id is None:
        self.subject_id = 0
      if self.type is None:
        self.type = ''
      if self.values is None:
        self.values = []
      if self.confidences is None:
        self.confidences = []
    else:
      self.subject_id = 0
      self.type = ''
      self.values = []
      self.confidences = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_Q.pack(self.subject_id))
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.values)
      buff.write(_struct_I.pack(length))
      for val1 in self.values:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.confidences)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.confidences))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 8
      (self.subject_id,) = _struct_Q.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8')
      else:
        self.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.values = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.values.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.confidences = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_Q.pack(self.subject_id))
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.values)
      buff.write(_struct_I.pack(length))
      for val1 in self.values:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.confidences)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.confidences.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 8
      (self.subject_id,) = _struct_Q.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8')
      else:
        self.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.values = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.values.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.confidences = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_Q = struct.Struct("<Q")
