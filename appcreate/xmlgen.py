import xml.dom.minidom
import os
import sys
import logging

def _loadtemplate(hv):
	if hv not in ('xen','kvm'):
		#logging.debug("Adding disk %s as %s/%s-%s.raws" % (item['name'], self.__imgdir,self.name, item['name']))
		logging.debug('Hypervisor %s not supported' % hv)
		return False
	else:
		fp = open('%s' % 
				(
				   os.path.join(os.getcwd(),'templates/%s.xml'%hv)		
				)
			)
		x = xml.dom.minidom.parse(fp)
		for e in x.childNodes:
			print dir(e)
_loadtemplate('kvm')
