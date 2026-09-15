---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I received the B.E. degree from the Department of Computer Science and Technology, University of Science and Technology Beijing (<a href="https://www.ustb.edu.cn/" target="_blank" rel="noopener">USTB</a>), in 2022, and I am currently pursuing the Ph.D. degree under the supervision of <a href="https://scce.ustb.edu.cn/info/1013/1010.htm" target="_blank" rel="noopener">Prof. Huimin Ma</a> at the 3D Image Lab. My research interests include:

<div class="tag-row">
  <span class="tag">Computer Vision</span>
  <span class="tag">3D Vision</span>
  <span class="tag">3D Controllable Generation &amp; Reconstruction</span>
  <span class="tag">Feed-forward 3DGS</span>
  <span class="tag">Autonomous Driving Simulation</span>
</div>

My work has led to <a href="/#-papers">10 papers</a> at conferences and journals including **CVPR, NeurIPS, ICCV, AAAI, ICASSP, IEEE TIP and IEEE TCSVT** — five of them as first or co-first author — together with two competition papers, and <a href="/#-honors-and-awards">national-level awards</a> including the first prize in the National College Student Mathematics Competition and a Finalist award in the ICM.

I completed a research internship at <a href="https://www.lixiang.com/" target="_blank" rel="noopener">Li Auto</a> and am currently working as a Physical AI Talent Program intern at <a href="https://www.xiaopeng.com/" target="_blank" rel="noopener">Xpeng Motors</a>. I lead the <a href="/#-research-projects">GSim</a> generative autonomous-driving simulator and take part in three national-level research projects, one of them as student lead.

<div class="notice notice--info" markdown="1">
**🔎 I am open to new opportunities.** I will receive my Ph.D. in June 2027 and am looking for full-time research roles in 3D vision, 3D generative models, and autonomous driving simulation. Feel free to reach me at <a href="mailto:yuhaochen_223@126.com">yuhaochen_223@126.com</a>.
</div>

# 🔥 News
- *2026.09*: &nbsp;💻 GSim, our generative autonomous-driving world simulator built on a pure 3DGS representation, will be open-sourced soon.
- *2026.06*: &nbsp;🚀 Joined Xpeng Motors as a Physical AI Talent Program Intern, working on feed-forward 3DGS reconstruction for the world simulator.
- *2026.02*: &nbsp;🎉🎉 Unposed-to-3D accepted by <font color="red">CVPR 2026</font>.
- *2025.12*: &nbsp;🚀 Joined Li Auto Inc. as a Research Intern, working on 3D asset adaptation for the autonomous-driving simulator.
- *2025.12*: &nbsp;🎉🎉 SPAR-GS accepted by <font color="red">ICASSP 2026</font>.
- *2025.09*: &nbsp;🎉🎉 MVSMamba accepted by <font color="red">NeurIPS 2025</font>.
- *2025.06*: &nbsp;🎉🎉 MonoMVSNet accepted by <font color="red">ICCV 2025</font>.
- *2024.12*: &nbsp;🎉🎉 HomuGAN accepted by <font color="red">TIP 2024</font>.
- *2024.12*: &nbsp;🎉🎉 ProtoCar accepted by <font color="red">AAAI 2025</font>.
- *2024.12*: &nbsp;🎉🎉 RRT-MVS accepted by <font color="red">AAAI 2025</font>.
- *2024.11*: &nbsp;🎉🎉 GET3DGS accepted by <font color="red">TCSVT 2024</font>. 



# 📝 Papers 


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/CVPR2026.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Unposed-to-3D: Learning Simulation-Ready Vehicles from Real-World Images](https://cvpr.thecvf.com/virtual/2026/poster/36385)

Hongyuan Liu, Bochao Zou, Qiankun Liu, **Haochen Yu**, Qi Mei, Jianfei Jiang, Chen Liu, Cheng Bi, Zhao Wang, Xueyang Zhang, Yifei Zhan, Jiansheng Chen, Huimin Ma

<img src=""> 
[**Project**](javascript:void(0))    [**Code**](javascript:void(0))    [**Paper**](https://arxiv.org/abs/2604.19257)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2026</div><img src='images/ICASSP2026.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SPAR-GS: Single-View Pose-Free Automobile Reconstruction with 3D Gaussian Splatting](https://ieeexplore.ieee.org/document/11464917)

Juntao Lyu†, **Haochen Yu**†, Hongyuan Liu, Qi Mei, Huimin Ma, Tianyu Hu

† *Co-first authors.*

<img src=""> 
[**Project**](javascript:void(0))    [**Code**](javascript:void(0))    [**Paper**](https://ieeexplore.ieee.org/document/11464917)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025.10</div><img src='images/gaucy.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GauCy: Hybrid Cylinder-Emissive Gaussian Splatting for 3D Sparse-View Driving Scenes Reconstruction](https://arxiv.org/pdf/2510.07856)

**Haochen Yu**, Qiankun Liu , Hongyuan Liu, Jianfei Jiang, Juntao Lyu, Jiansheng Chen, Huimin Ma

<img src=""> [**Project**](https://xyzc-ylinder-projectpage.vercel.app/)   [**Code**](https://github.com/yuyuyu223/XYZCylinder)    [**Paper**]()

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025.08</div><img src='images/instdrive.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015)

Hongyuan Liu†, **Haochen Yu**†, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma

† *Co-first authors.*

<img src=""> [**Project**](https://instdrive.github.io/)   [**Code**](#)    [**Paper**](https://arxiv.org/abs/2508.12015)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/mvsmamba.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MVSMamba: Multi-View Stereo with State Space Model](#)

Jianfei Jiang, Qiankun Liu, Hongyuan Liu, **Haochen Yu**, Liyong Wang, Jiansheng Chen, Huimin Ma

<img src=""> [**Project**](#)   [**Code**](https://github.com/JianfeiJ/MonoMVSNet)    [**Paper**](https://arxiv.org/pdf/2507.11333)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/monomvsnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MonoMVSNet: Monocular Priors Guided Multi-View Stereo Network](https://arxiv.org/abs/2507.11333)

Jianfei Jiang, Qiankun Liu, **Haochen Yu**, Hongyuan Liu, Liyong Wang, Jiansheng Chen, Huimin Ma

<img src=""> [**Project**](#)   [**Code**](https://github.com/JianfeiJ/MonoMVSNet)    [**Paper**](https://arxiv.org/pdf/2507.11333)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCSVT 2024</div><img src='images/TCSVT2024.jpeg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GET3DGS: Generate 3D Gaussians Based on Points Deformation Fields](https://ieeexplore.ieee.org/document/10777594)

**Haochen Yu**, Weixi Gong, Jiansheng Chen, Huimin Ma

<img src=""> [**Project**](https://yuyuyu223.github.io/GET3DGS-projectpage/)   [**Code**](https://gitee.com/HowsenFisher/get3-dgs)    [**Paper**](../assets/file/TCSVT-paper.pdf)
<!-- - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
</div>
</div>

- [H. Yu, W. Gong, J. Chen and H. Ma, "GET3DGS: Generate 3D Gaussians Based on Points Deformation Fields," in IEEE Transactions on Circuits and Systems for Video Technology, doi: 10.1109/TCSVT.2024.3511342.](https://ieeexplore.ieee.org/document/10777594) **TCSVT 2024**



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TIP 2024</div><img src='images/TIP2024.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

	
[HumoGAN: A 3D-aware GAN with the Method of Cylindrical Spatial-Constrained Sampling](https://ieeexplore.ieee.org/document/10816358)

**Haochen Yu**, Weixi Gong, Jiansheng Chen, Huimin Ma

<img src=""> 
[**Project**](https://yuyuyu223.github.io/homugan-projectpage/)    [**Code**](https://gitee.com/HowsenFisher/homugan)    [**Paper**](javascript:void(0))
<!-- - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
</div>
</div>

- [H. Yu, W. Gong, J. Chen and H. Ma, "HomuGAN: A 3D-Aware GAN With the Method of Cylindrical Spatial-Constrained Sampling," in IEEE Transactions on Image Processing, vol. 34, pp. 320-334, 2025, doi: 10.1109/TIP.2024.3520423.](https://ieeexplore.ieee.org/document/10816358) **TIP 2024**

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/aaai2025.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ProtoCar: Learning 3D Vehicle Prototypes from Single-View and Unconstrained driving scene Images](https://ojs.aaai.org/index.php/AAAI/article/view/32581)

Hongyuan Liu, **Haochen Yu**, Bochao Zou, Juntao Lyu, meiqi, Jiansheng Chen, Huimin Ma

<img src=""> 
[**Project**](javascript:void(0))    [**Code**](javascript:void(0))    [**Paper**](https://ojs.aaai.org/index.php/AAAI/article/view/32581)
<!-- - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/aaai2025_2.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RRT-MVS: Recurrent Regularization Transformer for Multi-View Stereo]([javascript:void(0)](https://ojs.aaai.org/index.php/AAAI/article/view/32418))

Jianfei Jiang, Liyong Wang, **Haochen Yu**, Tianyu Hu, Jiansheng Chen, Huimin Ma

<img src=""> 
[**Project**](javascript:void(0))    [**Code**](javascript:void(0))    [**Paper**]([javascript:void(0)](https://ojs.aaai.org/index.php/AAAI/article/view/32418))
<!-- - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->
</div>
</div>



# 📝 Competition Papers

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICM 2021</div><img src='images/meisai.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A multi-objective nonlinear optimization model; A improved grey prediction model with time delay; fuzzy comprehensive analysis method](../assets/file/美赛论文.pdf)

Zhang Yuwei, Chen Fangyi, Yu Haochen (*equal contribution*)

[**Paper**](../assets/file/美赛论文.pdf)
- Certificate of Achievement; Was Designated As Finalist
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Beidou Cup</div><img src='images/beidoubei.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A intelligent livestock management system based on BeiDou Navigation Satellite System](../assets/file/北斗论文.pdf)

Haochen Yu, Xueyuan Yang (*equal contribution*)

[**Paper**](../assets/file/北斗论文.pdf)
- In recognition of the first prize winner(s) of Tianjin Municipality (Undergraduate Group) 
- Submitted to the Twelfth BeiDou-Cup China Adolescents Science & Technology Invention Contest
</div>
</div>


# 🔨 Research Projects

<div class="info-card">
  <div class="card-icon"><img src="images/lab-mark.png" alt="3D Image Lab"></div>
  <div class="card-body">
    <div class="card-title">GSim: A Generative World Simulator for Autonomous Driving based on Hierarchical 3D Gaussian Generalized Nodes<span class="card-role">Project Lead</span></div>
    <div class="card-sub">3D Image Lab, USTB · companion paper targeted at TPAMI 2026, code to be open-sourced</div>
    <div class="card-note">The first 3DGS-only driving simulator: a scene graph with hierarchical 3D Gaussian generalized nodes unifies generation, editing and interaction, lifting downstream detection by 2–5% mAP.</div>
  </div>
  <div class="card-date">Present</div>
  <div class="icon-chip current" title="Ongoing"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 10 10 10-4.48 10-10S17.52 2 11.99 2z"/><path d="M12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg></div>
</div>

<div class="card-follow">
  <div class="card-fig"><img src="images/GSim.jpg" alt="GSim pipeline overview"></div>
  <div class="card-links"><a href="javascript:void(0)"><strong>Project</strong></a><a href="javascript:void(0)"><strong>Code</strong></a></div>
</div>

<div class="info-card">
  <div class="card-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19.8 18.4L14 10.67V6.5l1.35-1.69c.26-.33.03-.81-.39-.81H9.04c-.42 0-.65.48-.39.81L10 6.5v4.17L4.2 18.4c-.49.66-.02 1.6.8 1.6h14c.82 0 1.29-.94.8-1.6z"/></svg></div>
  <div class="card-body">
    <div class="card-title">Key Technologies for Multi-Agent Unified World Models<span class="card-role">Main Participant</span></div>
    <div class="card-sub">Beijing Natural Science Foundation – Shunyi Innovation Joint Fund</div>
    <div class="card-note">Feed-forward scene reconstruction and PBR rendering on top of the 3DGS simulator; generative 3D simulation platform and closed-loop pipeline.</div>
  </div>
  <div class="card-date">2025.06 – 2027.06</div>
  <div class="icon-chip current" title="Ongoing"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 10 10 10-4.48 10-10S17.52 2 11.99 2z"/><path d="M12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg></div>
</div>

<div class="info-card">
  <div class="card-icon"><img src="images/nsfc-mark.png" alt="National Natural Science Foundation of China"></div>
  <div class="card-body">
    <div class="card-title">Human-Factor Safety Monitoring Instrument for Mixed Autonomous Traffic Environments<span class="card-role">Main Participant</span></div>
    <div class="card-sub">National Natural Science Foundation of China – Major National Research Instrument Development Project</div>
    <div class="card-note">Mixed-traffic scene generation and closed-loop simulation carrier, fusing iterative 3DGS/4DGS reconstruction with GAN-, diffusion- and Image-to-3D-based agent generation.</div>
  </div>
  <div class="card-date">2023.09 – 2028.09</div>
  <div class="icon-chip current" title="Ongoing"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 10 10 10-4.48 10-10S17.52 2 11.99 2z"/><path d="M12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg></div>
</div>

<div class="info-card">
  <div class="card-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19.8 18.4L14 10.67V6.5l1.35-1.69c.26-.33.03-.81-.39-.81H9.04c-.42 0-.65.48-.39.81L10 6.5v4.17L4.2 18.4c-.49.66-.02 1.6.8 1.6h14c.82 0 1.29-.94.8-1.6z"/></svg></div>
  <div class="card-body">
    <div class="card-title">Photorealistic Data Synthesis for Autonomous Driving Scenes<span class="card-role">Student Lead</span></div>
    <div class="card-sub">National Science and Technology Major Project (2022ZD0116305) · closed</div>
    <div class="card-note">NeRF-GAN and 3DGS-GAN based single-asset generation, multi-object generation via 3DGS simulation, corner-case collection and dataset construction, and diffusion/LoRA fine-tuning for corner-case scenes.</div>
  </div>
  <div class="card-date">2022.12 – 2025.12</div>
  <div class="icon-chip ended" title="Completed"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div>
</div>

<div class="info-card">
  <div class="card-icon"><img src="images/nsfc-mark.png" alt="National Natural Science Foundation of China"></div>
  <div class="card-body">
    <div class="card-title">Few-Shot Cognitive Learning and Object Recognition under Uncertain Environments<span class="card-role">Participant</span></div>
    <div class="card-sub">National Natural Science Foundation of China – Joint Funds</div>
    <div class="card-note">Cognition-inspired few-shot learning serving autonomous driving and remote sensing; knowledge-and-data driven representations and weakly supervised segmentation in complex traffic scenes, +8.1% over baseline on Cityscapes.</div>
  </div>
  <div class="card-date">2021.01 – 2024.12</div>
  <div class="icon-chip ended" title="Completed"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div>
</div>

<div class="grant-note">Work in the group is also supported by the National Nature Science Foundation of China under Grant 62227801.</div>

# 🎖 Honors and Awards

<div class="award-grid">

  <div class="award-card level-intl">
    <div class="award-meta"><span class="award-level">International</span><span class="award-date">2021.04</span></div>
    <div class="award-name">Finalist Award (Problem E) in International Mathematical Modeling Competition (ICM)</div>
    <div class="award-org">Consortium for Mathematics and Its Applications</div>
  </div>
  <div class="award-card level-national">
    <div class="award-meta"><span class="award-level">National</span><span class="award-date">2021.07</span></div>
    <div class="award-name">First Prize in the 14th China College Student Computer Design Competition</div>
    <div class="award-org">China College Student Computer Design Competition Organizing Committee</div>
  </div>
  <div class="award-card level-national">
    <div class="award-meta"><span class="award-level">National</span><span class="award-date">2019.11</span></div>
    <div class="award-name">First Prize in the 11th National College Student Mathematics Competition</div>
    <div class="award-org">Chinese Mathematical Society</div>
  </div>
  <div class="award-card level-national">
    <div class="award-meta"><span class="award-level">National</span><span class="award-date">2021.04</span></div>
    <div class="award-name">Second Prize in National Finals of the 12th "Beidou Cup" National Youth Science and Technology Innovation Competition</div>
    <div class="award-org">China Satellite Navigation Conference Organizing Committee</div>
  </div>
  <div class="award-card level-region">
    <div class="award-meta"><span class="award-level">Regional</span><span class="award-date">2021.04</span></div>
    <div class="award-name">First Prize in North China Region of the 12th "Beidou Cup" National Youth Science and Technology Innovation Competition</div>
    <div class="award-org">China Satellite Navigation Conference Organizing Committee</div>
  </div>
  <div class="award-card level-region">
    <div class="award-meta"><span class="award-level">Municipal</span><span class="award-date">2019.12</span></div>
    <div class="award-name">First Prize in the 30th Beijing College Student Mathematics Competition</div>
    <div class="award-org">Beijing Mathematical Society</div>
  </div>
  <div class="award-card level-region">
    <div class="award-meta"><span class="award-level">Municipal</span><span class="award-date">2021.05</span></div>
    <div class="award-name">Second Prize in Beijing Computer Design Competition "Shuori Cup"</div>
    <div class="award-org">Beijing Computer Design Competition Organizing Committee</div>
  </div>
  <div class="award-card level-region">
    <div class="award-meta"><span class="award-level">Provincial</span><span class="award-date">2021.05</span></div>
    <div class="award-name">Third Prize in the 12th Blue Bridge Cup National Software and Information Technology Professional Talent Competition (Provincial Python Category)</div>
    <div class="award-org">Blue Bridge Cup Organizing Committee</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2021.09</span></div>
    <div class="award-name">First Prize in RoboCup Competition of USTB</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2021.04</span></div>
    <div class="award-name">First Prize in Computer Design Competition of USTB</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2021.04</span></div>
    <div class="award-name">First Prize in Student Research Training Program (SRTP) "Interactive Emotion Management System Based on Multimodal Emotion Recognition" Project</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2021.04</span></div>
    <div class="award-name">Second Prize in the 14th National College Students Energy Saving &amp; Emission Reduction Social Practice and Science Competition (USTB Division)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2021.04</span></div>
    <div class="award-name">Second Prize in Student Research Training Program (SRTP) "Supercapacitor" Project</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2020.11</span></div>
    <div class="award-name">Second Prize in RoboCup Competition (Category B) of USTB</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2019.12</span></div>
    <div class="award-name">Second Prize in Innovation Cup Competition of University of Science and Technology Beijing</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2019.06</span></div>
    <div class="award-name">Second Prize in Mathematics Competition of University of Science and Technology Beijing</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-school">
    <div class="award-meta"><span class="award-level">USTB</span><span class="award-date">2019.07</span></div>
    <div class="award-name">Third Prize in the 21st Cradle Cup Student Entrepreneurship Competition of USTB</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Scholarship</span><span class="award-date">2021.11</span></div>
    <div class="award-name">Second-Class People's Scholarship of USTB (2020-2021)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Honor</span><span class="award-date">2021.11</span></div>
    <div class="award-name">Outstanding Communist Youth League Member of USTB (2020-2021)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Scholarship</span><span class="award-date">2020.11</span></div>
    <div class="award-name">Second-Class People's Scholarship of USTB (2019-2020)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Honor</span><span class="award-date">2020.11</span></div>
    <div class="award-name">Outstanding Student Award of USTB (2019-2020)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Scholarship</span><span class="award-date">2019.11</span></div>
    <div class="award-name">Second-Class People's Scholarship of USTB (2018-2019)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Honor</span><span class="award-date">2019.11</span></div>
    <div class="award-name">Outstanding Student Award of USTB (2018-2019)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Scholarship</span><span class="award-date">2019.05</span></div>
    <div class="award-name">Third-Class People's Scholarship for Freshmen of USTB (2018-2019)</div>
    <div class="award-org">USTB</div>
  </div>
  <div class="award-card level-honor">
    <div class="award-meta"><span class="award-level">Honor</span><span class="award-date">2019.12</span></div>
    <div class="award-name">Outstanding Individual in "College Student Social Practice" of USTB</div>
    <div class="award-org">USTB</div>
  </div>

</div>

# 📖 Educations

<div class="info-card">
  <div class="card-badge"><img src="images/ustb-badge.png" alt="USTB badge"></div>
  <div class="card-body">
    <div class="card-title">University of Science and Technology Beijing (USTB)<span class="card-role">Ph.D.</span></div>
    <div class="card-sub">Computer Science and Technology</div>
    <div class="card-note">Direct Ph.D. admission by recommendation, top 3.75% (6/160) of the cohort · USTB "Merit Student" (三好研究生) · Beijing, China</div>
  </div>
  <div class="card-date">2022.09 – 2027.06</div>
  <div class="icon-chip" title="Doctor of Philosophy"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3z"/><path d="M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"/></svg></div>
</div>

<div class="info-card">
  <div class="card-badge"><img src="images/ustb-badge.png" alt="USTB badge"></div>
  <div class="card-body">
    <div class="card-title">University of Science and Technology Beijing (USTB)<span class="card-role">B.E.</span></div>
    <div class="card-sub">Computer Science and Technology</div>
    <div class="card-note">Graduated as an "Outstanding Graduate" of USTB · Beijing, China</div>
  </div>
  <div class="card-date">2018.09 – 2022.07</div>
  <div class="icon-chip" title="Bachelor of Engineering"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg></div>
</div>

# 💻 Internships

<div class="info-card">
  <div class="company-logo"><img src="images/logo-xiaopeng.png" alt="Xpeng logo"></div>
  <div class="card-body">
    <div class="card-title">Xpeng Motors Inc.<span class="card-role">Physical AI Talent Program Intern</span></div>
    <div class="card-sub">Space Algorithm Group, Data Engine Department · Guangzhou, China</div>
    <div class="card-note">Feed-forward 3DGS reconstruction pipeline for the world simulator; multi-camera fusion reconstruction under inconsistent exposure and ISP colour bias.</div>
  </div>
  <div class="card-date">2026.06 – present</div>
  <div class="icon-chip current" title="Ongoing"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 10 10 10-4.48 10-10S17.52 2 11.99 2z"/><path d="M12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg></div>
</div>

<div class="info-card">
  <div class="company-logo"><img src="images/logo-lixiang.png" alt="Li Auto logo"></div>
  <div class="card-body">
    <div class="card-title">Li Auto Inc.<span class="card-role">Research Intern (Foundation Model)</span></div>
    <div class="card-sub">Space Reconstruction Team, Action Intelligence, Foundation Model Department · Beijing, China</div>
    <div class="card-note">3D asset adaptation for the autonomous-driving simulator; produced LUMEN-GS, a light-disentangled feed-forward 3D Gaussian Splatting model, submitted to NeurIPS 2026.</div>
  </div>
  <div class="card-date">2025.12 – 2026.06</div>
  <div class="icon-chip ended" title="Completed"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div>
</div>
