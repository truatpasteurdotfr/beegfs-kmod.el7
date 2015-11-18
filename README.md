# beegfs-kmod.el7
Building the beegfs-client kernel module for RHEL7/clones

Initial version built for CentOS-7.1 3.10.0-229.el7

Work based on the elrepo/templates/el7 at https://github.com/elrepo/templates.git

Disable the autobuild feature:
```
# sed -i -e 's/^buildEnabled=true/buildEnabled=false/g' /etc/beegfs/beegfs-client-autobuild.conf
```
The sources have been pulled by doing:
```
# rpm2cpio beegfs-client-2015.03.r7-el6.noarch.rpm | cpio -iudv
# cd opt/beegfs/src/client && tar cjvf beegfs-2015.03.r7.tar.bz2 beegfs_client_module_2015.03
```
YMMV, use at your own risks.

Tru
