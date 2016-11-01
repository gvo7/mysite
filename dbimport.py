from inventory.models import Type
Type.objects.create(name='router')
Type.objects.create(name='switch')
Type.objects.create(name='bladeswitch')
Type.objects.create(name='access-switch')
Type.objects.create(name='firewall')
Type.objects.create(name='vpn-gateway')
Type.objects.create(name='enclosure')
Type.objects.create(name='bladeserver')
Type.objects.create(name='adc')
Type.objects.create(name='swg')
Type.objects.create(name='wifi-controller')
Type.objects.create(name='wifi-ap')

from inventory.models import Team
Team.objects.create(name='Telco Extranet', email='telco.extranet@mail.com', business_phone='+3211223344', standby_phone='+3211223345', teamleader='TL Telco Extranet', sdo='SDO Telco Extranet')
Team.objects.create(name='Telco DC', email='telco.dc@mail.com', business_phone='+3211223354', standby_phone='+3211223355', teamleader='TL Telco DC', sdo='SDO Telco DC')
Team.objects.create(name='Telco eWorkplace', email='telco.eworkplace@mail.com', business_phone='+3211223364', standby_phone='+3211223365', teamleader='TL Telco eWorkplace', sdo='SDO eWorkplace')
Team.objects.create(name='Telco Omnichannels', email='telco.omnichannels@mail.com', business_phone='+3211223374', standby_phone='+3211223375', teamleader='TL Telco Omnichannels', sdo='SDO Omnichannels')

from inventory.models import Vendor
Vendor.objects.create(name='Pulse Secure', email_support='support@pulsesecure.net', account_manager='Account Manager', email_account_manager='accountmgr@pulsesecure.net', service_manager='Service Manager', email_service_manager='servicemgr@pulsesecure.net', contract_number='ps1234')
Vendor.objects.create(name='McAfee', email_support='support@mcafee.com', account_manager='Account Manager', email_account_manager='accountmgr@mcafee.com', service_manager='Service Manager', email_service_manager='servicemgr@mcafee.com', contract_number='mc12345')
Vendor.objects.create(name='Akamai', email_support='support@akamai.com', account_manager='Account Manager', email_account_manager='accountmgr@akamai.com', service_manager='Service Manager', email_service_manager='servicemgr@akamai.com', contract_number='plx-12345')
Vendor.objects.create(name='F5 Networks', email_support='support@f5.com', account_manager='Account Manager', email_account_manager='accountmgr@f5.com', service_manager='Service Manager', email_service_manager='servicemgr@f5.com', contract_number='f5-contr00123123')
Vendor.objects.create(name='Palo Alto Networks', email_support='support@pan.com', account_manager='Account Manager', email_account_manager='accountmgr@pan.com', service_manager='Service Manager', email_service_manager='servicemgr@pan.com', contract_number='pan-contr00123123')
Vendor.objects.create(name='Cisco', email_support='support@cisco.com', account_manager='Account Manager', email_account_manager='accountmgr@cisco.com', service_manager='Service Manager', email_service_manager='servicemgr@cisco.com', contract_number='cisco-cnr0929233')
Vendor.objects.create(name='Interoute', email_support='support@interoute.com', account_manager='Account Manager', email_account_manager='accountmgr@interoute.com', service_manager='Service Manager', email_service_manager='servicemgr@interoute.com', contract_number='iroute-CF12345')
Vendor.objects.create(name='Telenet', email_support='support@telenet.be', account_manager='Account Manager', email_account_manager='accountmgr@telenet.be', service_manager='Service Manager', email_service_manager='servicemgr@telenet.be', contract_number='telenet-1234ABDE')

from inventory.models import Integrator
Integrator.objects.create(name='Securelink', email_support='support@securelink.be', account_manager='Account Manager', email_account_manager='accountmgr@securelink.be', service_manager='Service Manager', email_service_manager='servicemgr@securelink.be', contract_number='sec-12345')
Integrator.objects.create(name='Proximus', email_support='support@proximus.be', account_manager='Account Manager', email_account_manager='accountmgr@proximus.be', service_manager='Service Manager', email_service_manager='servicemgr@proximus.be', contract_number='proxi-12345')
Integrator.objects.create(name='Dimension Data', email_support='support@dimensiondata.com', account_manager='Account Manager', email_account_manager='accountmgr@dimensiondata.com', service_manager='Service Manager', email_service_manager='servicemgr@dimensiondata.com', contract_number='didata-12345')

from inventory.models import Service_status
Service_status.objects.create(name='in_stock')
Service_status.objects.create(name='install/configure')
Service_status.objects.create(name='in_transit')
Service_status.objects.create(name='staging/pre-production')
Service_status.objects.create(name='production')
Service_status.objects.create(name='maintenance')
Service_status.objects.create(name='decommission')

from inventory.models import Configuration_owner
Configuration_owner.objects.create(name='Telco Extranet')
Configuration_owner.objects.create(name='Telco DC')
Configuration_owner.objects.create(name='Telco eWorkplace')
Configuration_owner.objects.create(name='Telco Omnichannels')

from inventory.models import Management
Management.objects.create(name='SSH')
Management.objects.create(name='Rest API')
Management.objects.create(name='Algosec')
Management.objects.create(name='CiscoPrime')
Management.objects.create(name='Ansible')
Management.objects.create(name='Puppet')
Management.objects.create(name='Chef')

from inventory.models import Product
Product.objects.create(vendor='Pulse Secure', product_name='SA2500', type='vpn-gateway', logging_template='R:\I2B\Telecom\Template\Logging\ps-sa2500', monitoring_template='R:\I2B\Telecom\Template\Monitoring\ps-sa2500')


