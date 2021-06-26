
# infrastructure-validation
Validation of infrastucture after successful provisiong with Ansible connection, can use multiple connection types for more info refer testinfra documentation, in this repo consuming Ansible connection to ssh on nodes/hosts.

**Pre-reqs:**
1. Install Ansible.
2. Install testinfra and pytest via pip refer: https://testinfra.readthedocs.io
3. Provision one ore two nodes/hosts via Ansible/any IAAC/manually.
4. Create inventory file as below
   cat /etc/ansible/hosts
   [web]
   web01

   [app]
   app01
 5. Make sure hosts are connecting via Ansible connection.
  
 **Validate code** 
 1. Check coding standards
    #pycodestyle test_bstack.py
    
 2. Validate connectvity from Ansible host to nodes/hosts 
    #ansible all -m ping
    
 **Execution**
 #pytest  --hosts web--ansible-inventory=/etc/ansible/hosts --connection=ansible -m infra -n 2  test_mystack.py

--hosts web Execute tests on ansible inventory group called web

 --connection ansible (leverage ansible connection to execute the commands on destination hosts)

--n number of parallel executions
