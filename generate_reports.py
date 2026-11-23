import os
import subprocess
from docx import Document
from docx.shared import Pt

def create_study_report():
    doc = Document()
    doc.add_heading('Ethernet Communication and Network Protocols Study Report', 0)
    
    doc.add_paragraph('Author: Siddharth Dere\nRole: Network Engineer\n')
    
    doc.add_heading('1. Ethernet Architecture and Frame Structure', level=1)
    doc.add_paragraph('Ethernet operates at the Data Link and Physical layers of the OSI model. The standard IEEE 802.3 Ethernet frame consists of the following components:')
    
    components = [
        "Preamble & SFD (Start Frame Delimiter): 8 bytes used for clock synchronization.",
        "Destination MAC Address: 6 bytes identifying the intended receiver's NIC.",
        "Source MAC Address: 6 bytes identifying the sender's NIC.",
        "EtherType: 2 bytes indicating the encapsulated payload protocol (e.g., IPv4 is 0x0800).",
        "Payload: The encapsulated data from higher layers (46 to 1500 bytes).",
        "FCS (Frame Check Sequence): 4 bytes containing a CRC to detect transmission errors."
    ]
    for item in components:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_heading('2. Addressing Mechanisms', level=1)
    doc.add_paragraph('MAC (Media Access Control) Addressing: A 48-bit physical address burned into the Network Interface Card (NIC). It operates at Layer 2 and is only locally significant.\n'
                      'IPv4 Addressing: A 32-bit logical address operating at Layer 3 allowing for routing across different network boundaries.')

    doc.add_heading('3. Transport and Network Layer Protocols', level=1)
    protocols = [
        "TCP: Connection-oriented Layer 4 protocol. Guarantees delivery and order.",
        "UDP: Connectionless Layer 4 protocol. Prioritizes speed over reliability.",
        "ARP: Layer 2/3 bridge protocol. Resolves IP addresses to MAC addresses.",
        "ICMP: Layer 3 network diagnostic protocol, used by ping for reachability."
    ]
    for item in protocols:
        doc.add_paragraph(item, style='List Bullet')

    docx_path = 'docs/Study_Report.docx'
    doc.save(docx_path)
    return docx_path

def create_analysis_report():
    doc = Document()
    doc.add_heading('Network Traffic Analysis and Diagnostics Report', 0)
    doc.add_paragraph('Author: Siddharth Dere\n')
    
    doc.add_heading('1. Difference Between MAC and IP Addresses', level=1)
    doc.add_paragraph('Based on the network captures, the logical IPv4 address of the local machine is 10.171.157.142, while the default gateway operates at 10.171.157.60. Physical frame delivery relies on Layer 2 MAC addresses. The Intel NIC MAC address is b0:47:e9:ec:8f:33, and the gateway MAC is 46:54:40:8a:9e:1f. The MAC address changes at every router hop, while the IP address remains constant end-to-end.')

    doc.add_heading('2. Difference Between TCP and UDP Protocols', level=1)
    doc.add_paragraph('In the captured DNS traffic utilizing UDP, the machine sent a standard query using random ephemeral source port 42003 and destination port 53. The server responded immediately without a connection setup phase. This connectionless behavior makes UDP ideal for rapid telemetry streams.')

    doc.add_heading('3. Purpose of the ARP Protocol', level=1)
    doc.add_paragraph('When the ARP cache was flushed, Wireshark captured an ARP Request: "Who has 10.171.157.60? Tell 10.171.157.142". The gateway responded with a unicast ARP Reply: "10.171.157.60 is at 46:54:40:8a:9e:1f".')

    doc.add_heading('4. Packet Flow During a Ping Operation', level=1)
    doc.add_paragraph('The local machine encapsulates an ICMP Echo Request inside an IPv4 packet destined for the target IP. The target receives the payload, processes it, and generates an ICMP Echo Reply, reversing the source and destination IP/MAC addresses.')

    docx_path = 'docs/Analysis_Report.docx'
    doc.save(docx_path)
    return docx_path

def convert_to_pdf(docx_path):
    print(f"Converting {docx_path} to PDF via LibreOffice...")
    # Run Ubuntu's native LibreOffice in headless mode to render the PDF
    subprocess.run([
        "libreoffice", "--headless", "--convert-to", "pdf", 
        docx_path, "--outdir", "docs"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Success: PDF generated in docs/")

if __name__ == "__main__":
    os.makedirs('docs', exist_ok=True)
    
    print("Building Word Documents...")
    study_docx = create_study_report()
    analysis_docx = create_analysis_report()
    
    convert_to_pdf(study_docx)
    convert_to_pdf(analysis_docx)
    
    # Optional cleanup: remove the .docx files if you only want the PDFs in your repo
    os.remove(study_docx)
    os.remove(analysis_docx)
    print("Complete! Ready to push to GitHub.")
