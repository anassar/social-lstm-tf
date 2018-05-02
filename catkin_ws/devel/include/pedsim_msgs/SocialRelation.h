// Generated by gencpp from file pedsim_msgs/SocialRelation.msg
// DO NOT EDIT!


#ifndef PEDSIM_MSGS_MESSAGE_SOCIALRELATION_H
#define PEDSIM_MSGS_MESSAGE_SOCIALRELATION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pedsim_msgs
{
template <class ContainerAllocator>
struct SocialRelation_
{
  typedef SocialRelation_<ContainerAllocator> Type;

  SocialRelation_()
    : type()
    , strength(0.0)
    , track1_id(0)
    , track2_id(0)  {
    }
  SocialRelation_(const ContainerAllocator& _alloc)
    : type(_alloc)
    , strength(0.0)
    , track1_id(0)
    , track2_id(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _type_type;
  _type_type type;

   typedef float _strength_type;
  _strength_type strength;

   typedef uint32_t _track1_id_type;
  _track1_id_type track1_id;

   typedef uint32_t _track2_id_type;
  _track2_id_type track2_id;


    static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TYPE_SPATIAL;
     static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TYPE_ROMANTIC;
     static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TYPE_PARENT_CHILD;
     static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  TYPE_FRIENDSHIP;
 

  typedef boost::shared_ptr< ::pedsim_msgs::SocialRelation_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pedsim_msgs::SocialRelation_<ContainerAllocator> const> ConstPtr;

}; // struct SocialRelation_

typedef ::pedsim_msgs::SocialRelation_<std::allocator<void> > SocialRelation;

typedef boost::shared_ptr< ::pedsim_msgs::SocialRelation > SocialRelationPtr;
typedef boost::shared_ptr< ::pedsim_msgs::SocialRelation const> SocialRelationConstPtr;

// constants requiring out of line definition

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      SocialRelation_<ContainerAllocator>::TYPE_SPATIAL =
        
          "\"spatial\""
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      SocialRelation_<ContainerAllocator>::TYPE_ROMANTIC =
        
          "\"romantic\""
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      SocialRelation_<ContainerAllocator>::TYPE_PARENT_CHILD =
        
          "\"parent_child\""
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      SocialRelation_<ContainerAllocator>::TYPE_FRIENDSHIP =
        
          "\"friendship\""
        
        ;
   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pedsim_msgs::SocialRelation_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pedsim_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/indigo/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'pedsim_msgs': ['/home/BB/catkin_ws/src/pedsim_ros/pedsim_msgs/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pedsim_msgs::SocialRelation_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pedsim_msgs::SocialRelation_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pedsim_msgs::SocialRelation_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
{
  static const char* value()
  {
    return "004e9c919342c749d66dbc051dba51f6";
  }

  static const char* value(const ::pedsim_msgs::SocialRelation_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x004e9c919342c749ULL;
  static const uint64_t static_value2 = 0xd66dbc051dba51f6ULL;
};

template<class ContainerAllocator>
struct DataType< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pedsim_msgs/SocialRelation";
  }

  static const char* value(const ::pedsim_msgs::SocialRelation_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string      type        # e.g. mother-son relationship, romantic relationship, etc.\n\
float32     strength    # relationship strength between 0.0 and 1.0\n\
\n\
uint32      track1_id\n\
uint32      track2_id\n\
\n\
\n\
# Constants for type (just examples at the moment)\n\
string      TYPE_SPATIAL  = \"spatial\"\n\
string      TYPE_ROMANTIC = \"romantic\"\n\
string      TYPE_PARENT_CHILD = \"parent_child\"\n\
string      TYPE_FRIENDSHIP = \"friendship\"\n\
";
  }

  static const char* value(const ::pedsim_msgs::SocialRelation_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.type);
      stream.next(m.strength);
      stream.next(m.track1_id);
      stream.next(m.track2_id);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SocialRelation_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pedsim_msgs::SocialRelation_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pedsim_msgs::SocialRelation_<ContainerAllocator>& v)
  {
    s << indent << "type: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.type);
    s << indent << "strength: ";
    Printer<float>::stream(s, indent + "  ", v.strength);
    s << indent << "track1_id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.track1_id);
    s << indent << "track2_id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.track2_id);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PEDSIM_MSGS_MESSAGE_SOCIALRELATION_H
