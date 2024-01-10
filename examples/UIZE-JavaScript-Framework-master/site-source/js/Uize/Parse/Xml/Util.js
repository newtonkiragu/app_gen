/*______________
|       ______  |   U I Z E    J A V A S C R I P T    F R A M E W O R K
|     /      /  |   ---------------------------------------------------
|    /    O /   |    MODULE : Uize.Parse.Xml.Util Package
|   /    / /    |
|  /    / /  /| |    ONLINE : http://www.uize.com
| /____/ /__/_| | COPYRIGHT : (c)2014-2016 UIZE
|          /___ |   LICENSE : Available under MIT License or GNU General Public License
|_______________|             http://www.uize.com/license.html
*/

/* Module Meta Data
	type: Package
	importance: 2
	codeCompleteness: 40
	docCompleteness: 2
*/

/*?
	Introduction
		The =Uize.Parse.Xml.Util= module provides utility methods for working with parser class trees generated by the various parsing objects under the =Uize.Parse.Xml= namespace.

		*DEVELOPERS:* `Chris van Rensburg`
*/

Uize.module ({
	name:'Uize.Parse.Xml.Util',
	required:[
		'Uize.Data.Matches',
		'Uize.Parse.Xml.TagAttribute'
	],
	builder:function () {
		'use strict';

		var
			/*** references to methods used internally ***/
				_isTag,
				_getAttribute,
				_getAttributeValue
		;

		return Uize.package ({
			findNodeByTagName:function (_nodeList,_tagName) {
				return Uize.findRecord (_nodeList.nodes,function (_node) {return _isTag (_node,_tagName)});
			},

			isTag:_isTag = function (_node,_tagName) {
				return _node.tagName && _node.tagName.serialize () == _tagName;
			},

			getTagById:function (_nodeList,_id) {
				var _idMatcher = typeof _id == 'string'
					? function (_nodeId) {return _nodeId == _id}
					: Uize.resolveMatcher (_id)
				;
				return Uize.findRecord (
					_nodeList,
					function (_node) {return !!_node.tagName && _idMatcher (_getAttributeValue (_node,'id'))}
				);
			},

			getText:function (_node) {
				var
					_childNodes = _node && _node.childNodes,
					_textNode = _childNodes && _childNodes.nodes [0]
				;
				return _textNode ? _textNode.text : '';
			},

			getTags:function (_nodeList,_tagName) {
				return Uize.Data.Matches.values (
					_nodeList.nodes,
					function (_node) {return _isTag (_node,_tagName)}
				);
			},

			getAttribute:_getAttribute = function (_node,_attributeName) {
				return Uize.findRecord (
					_node.tagAttributes.attributes,
					function (_attribute) {return _attribute.name.name == _attributeName}
				);
			},

			getAttributeValue:_getAttributeValue = function (_node,_attributeName) {
				var _attribute = _getAttribute (_node,_attributeName);
				return _attribute ? _attribute.value.value : '';
			},

			setAttributeValue:function (_node,_attributeName,_attributeValue) {
				var _attribute = _getAttribute (_node,_attributeName);
				_attribute ||
					_node.tagAttributes.attributes.push (
						_attribute = new Uize.Parse.Xml.TagAttribute (_attributeName + '=""')
					)
				;
				if (_attributeValue != undefined)
					_attribute.value.value = _attributeValue
				;
				return _attribute;
			},

			recurseNodes:function (_node,_nodeHandler) {
				function _processNode (_node,_nodeNo,_nodes) {
					var _result = _nodeHandler (_node,_nodeNo,_nodes);
					if (_result !== false) {
						var _childNodes = _node.childNodes;
						_childNodes && Uize.forEach (_childNodes.nodes,_processNode);
					}
				}
				_processNode (_node);
			}
		});
	}
});
