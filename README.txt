This is a python script. 

Background information to this script is available in my Linkedin Article: https://tinyurl.com/y532dw7z

Feel free to share and provide feedback for improvement!

1. This script accept session list output from Fortigate 'diag sys session list'
2. It parses the output using 're module and collections module'
3. Outputs a text file containing the summary of the session list

// No offload reason and it's count - already added to script
// Protocols seen in the session list and it's count - already added to script
// NPU Error - already added to script
// Top IP address - yet to add to script
// Top Protocol - yet to add to script



Sample Output:

The number of sessions which are not offloaded, along with it's reason:
=======================================================================

('no_ofld_reason:  dirty disabled-by-policy', 3)
('no_ofld_reason:  npu-flag-off', 9)
('no_ofld_reason:  dirty non-npu-intf', 27)
('no_ofld_reason:  offload-denied non-npu-intf', 207)
('no_ofld_reason:  local not-established', 240)
('no_ofld_reason:  dirty', 3485)
('no_ofld_reason:  non-npu-intf', 4126)
('no_ofld_reason:  local', 12762)
('no_ofld_reason:  dirty helper', 13324)
('no_ofld_reason:  offload-denied helper', 15786)
('no_ofld_reason:  helper', 17291)
('no_ofld_reason:  disabled-by-policy', 37128)
('no_ofld_reason:', 1239834)


The protocols seen in the session list, along with it's count: 
============================================================== 
 
('proto=89', 64)
('proto=1', 5131)
('proto=47', 80029)
('proto=17', 654907)
('proto=6', 697686)


The npu errors seen in the session list, along with it's count:
============================================================== 
 
('npu_state_err=20/20', 1)
('npu_state_err=01/00', 3)
('npu_state_err=04/20', 9)
('npu_state_err=00/01', 29)
('npu_state_err=04/04', 39)
('npu_state_err=20/04', 70)
('npu_state_err=00/05', 97)
('npu_state_err=00/24', 528)
('npu_state_err=20/00', 2098)
('npu_state_err=04/00', 44605)
('npu_state_err=00/20', 85620)
('npu_state_err=00/04', 416996)
('npu_state_err=00/00', 586122)
