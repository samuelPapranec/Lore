## Mac Address Changer
Changing MAC address makes me anonymous on the network 
mac addresses are often used by filters to allow or prevent devices in the network and allow devices to do specific tasks in the network - bypass filters, impersonate devices, hide identity 
`$ifconfig` - lists all network interfaces in device and *informations about each device <sup>[[1]]()</sup>*
1. **`>eth0`** is a virtual box, using NAT network
2. **`>lo`** virtual env created by linux
3. **`>wlan0`** external USB wireless adapter - 🔌(not included) needed for some of the attacks

<sup>[[1]]()</sup> :
1. If the device is connected to a network it will show its IP address 
2. [**netmask**](A Netmask is a 32-bit "mask" used to divide an IP address into subnets and specify the network's available hosts.) address
3. broadcast address
4. **ether** mac address - option that we want to modify 

**1)**`$ ifconfig eth0 down`    - disable network interface to be able to modify its options (if you see no errors that means command got executed properly)<br>

**2)** `$ ifconfig eth0 hw ether 9c:8a:a7:cc:aa:32` - changes mac address to any mac address (if you see no errors that means command got executed properly)
*  Traditional MAC addresses are 12-digit (6 bytes or 48 bits) hexadecimal numbers. 

**3)** `$ ifconfig eth0 up` - enable network interface (if you see no errors that means command got executed properly)









