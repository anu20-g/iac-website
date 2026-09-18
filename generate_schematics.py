import os

out_dir = r'c:\Users\Anurag Tewary\Documents\TRDL\iac_website\assets'
os.makedirs(out_dir, exist_ok=True)

# 1. MLA Firewall Schematic (TRDL <-> IAC <-> Enterprise)
svg_mla = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" height="100%" style="background:#050505; border:1px solid #333333; display:block;">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#111111" stroke-width="1"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#F5F5DC"/>
    </marker>
    <marker id="arrow-dim" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#777777"/>
    </marker>
  </defs>

  <rect width="100%" height="100%" fill="url(#grid)"/>

  <!-- Top Reference Bar -->
  <rect x="0" y="0" width="920" height="28" fill="#0a0a0a" stroke="#333333" stroke-width="1"/>
  <text x="16" y="18" fill="#888888" font-family="'Roboto Mono', monospace" font-size="10" letter-spacing="1.5">FIG 01 // ARCHITECTURAL FIREWALL AND SUB-LICENSING DATAFLOW</text>
  <text x="730" y="18" fill="#555555" font-family="'Roboto Mono', monospace" font-size="10">REF: MLA-TRDL-IAC-SPEC</text>

  <!-- SILO 1: TRDL -->
  <rect x="30" y="55" width="245" height="225" fill="#000000" stroke="#F5F5DC" stroke-width="1.5"/>
  <rect x="30" y="55" width="245" height="28" fill="#161616" stroke="#333333" stroke-width="1"/>
  <text x="42" y="73" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="11" font-weight="bold">TRDL (CORE R AND D LAB)</text>
  <text x="42" y="103" fill="#888888" font-family="'Roboto Mono', monospace" font-size="9">JURISDICTION: INDIA [SILOED]</text>
  <line x1="42" y1="112" x2="263" y2="112" stroke="#222222" stroke-width="1"/>
  <text x="42" y="132" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Pre-Geometric IDM Calculus</text>
  <text x="42" y="152" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Foundational Source Code</text>
  <text x="42" y="172" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Weight Matrices and Solvers</text>
  <text x="42" y="192" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Sovereign Core Patents</text>
  <rect x="42" y="222" width="221" height="35" fill="#0d0d0d" stroke="#333333" stroke-width="1"/>
  <text x="52" y="244" fill="#ff5555" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="bold">[ZERO EXTERNAL DIRECT ACCESS]</text>

  <!-- CONNECTOR 1: Master License Agreement -->
  <line x1="275" y1="145" x2="333" y2="145" stroke="#F5F5DC" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="281" y="135" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5">MLA GRANT</text>

  <!-- SILO 2: IAC -->
  <rect x="335" y="55" width="255" height="225" fill="#000000" stroke="#F5F5DC" stroke-width="2"/>
  <rect x="335" y="55" width="255" height="28" fill="#F5F5DC" stroke="#F5F5DC" stroke-width="1"/>
  <text x="347" y="73" fill="#000000" font-family="'Roboto Mono', monospace" font-size="11" font-weight="bold">IAC (LICENSING VEHICLE)</text>
  <text x="347" y="103" fill="#888888" font-family="'Roboto Mono', monospace" font-size="9">COMMERCIAL ENFORCEMENT</text>
  <line x1="347" y1="112" x2="578" y2="112" stroke="#222222" stroke-width="1"/>
  <text x="347" y="132" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ B2B Sub-Licensing Gate</text>
  <text x="347" y="152" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Royalty Ledger Auditing</text>
  <text x="347" y="172" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Field-of-Use Verification</text>
  <text x="347" y="192" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="9.5">+ Continuous Telemetry Probe</text>
  <rect x="347" y="222" width="231" height="35" fill="#0d0d0d" stroke="#333333" stroke-width="1"/>
  <text x="355" y="244" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="bold">[CLOSED-CAPITAL FIREWALL]</text>

  <!-- CONNECTOR 2: Sub-License -->
  <line x1="590" y1="145" x2="648" y2="145" stroke="#F5F5DC" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="596" y="135" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5">SUB-LICENSE</text>

  <!-- SILO 3: ENTERPRISE -->
  <rect x="650" y="55" width="240" height="225" fill="#000000" stroke="#555555" stroke-width="1.5"/>
  <rect x="650" y="55" width="240" height="28" fill="#161616" stroke="#333333" stroke-width="1"/>
  <text x="662" y="73" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="11" font-weight="bold">ENTERPRISE LICENSEE</text>
  <text x="662" y="103" fill="#888888" font-family="'Roboto Mono', monospace" font-size="9">RESTRICTED RUNTIME</text>
  <line x1="662" y1="112" x2="878" y2="112" stroke="#222222" stroke-width="1"/>
  <text x="662" y="132" fill="#999999" font-family="'Roboto Mono', monospace" font-size="9.5">+ Sandboxed Framework Node</text>
  <text x="662" y="152" fill="#999999" font-family="'Roboto Mono', monospace" font-size="9.5">+ Specific Commercial Task</text>
  <text x="662" y="172" fill="#999999" font-family="'Roboto Mono', monospace" font-size="9.5">+ Monitored Core Counts</text>
  <text x="662" y="192" fill="#999999" font-family="'Roboto Mono', monospace" font-size="9.5">+ Cryptographic Runtime Key</text>
  <rect x="662" y="222" width="216" height="35" fill="#0d0d0d" stroke="#333333" stroke-width="1"/>
  <text x="672" y="244" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5">[NO RE-DISTRIBUTION]</text>

  <!-- RECIPROCAL GRANT-BACK RETURN LOOP -->
  <path d="M 770 280 L 770 305 L 152 305 L 152 282" fill="none" stroke="#777777" stroke-dasharray="4,3" stroke-width="1.5" marker-end="url(#arrow-dim)"/>
  <text x="350" y="300" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5" letter-spacing="1">MANDATORY RECIPROCAL DERIVATIVE GRANT-BACK LOOP TO TRDL</text>
</svg>'''

with open(os.path.join(out_dir, 'schematic_mla_firewall.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_mla.strip())

# 2. VORASHI Technical Architecture Schematic
svg_vorashi = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 230" width="100%" height="100%" style="background:#050505; border:1px solid #333333; display:block;">
  <defs>
    <pattern id="vgrid" width="15" height="15" patternUnits="userSpaceOnUse">
      <path d="M 15 0 L 0 0 0 15" fill="none" stroke="#0e0e0e" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#vgrid)"/>
  <rect x="0" y="0" width="420" height="24" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="10" y="16" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5" letter-spacing="1">FIG 02A // VORASHI STABILITY HYSTERESIS SPEC</text>
  
  <!-- Core Hysteresis Loop Diagram -->
  <rect x="15" y="38" width="180" height="175" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="23" y="54" fill="#888888" font-family="'Roboto Mono', monospace" font-size="7.5">HYSTERESIS MEMORY LOOP</text>
  
  <!-- Hysteresis curve -->
  <path d="M 35 165 C 35 90, 110 75, 175 75" fill="none" stroke="#F5F5DC" stroke-width="1.5"/>
  <path d="M 175 75 C 175 150, 95 165, 35 165" fill="none" stroke="#777777" stroke-dasharray="3,2" stroke-width="1.2"/>
  <line x1="25" y1="120" x2="185" y2="120" stroke="#222222" stroke-width="1"/>
  <line x1="105" y1="58" x2="105" y2="182" stroke="#222222" stroke-width="1"/>
  <text x="145" y="114" fill="#555555" font-family="'Roboto Mono', monospace" font-size="7">+Stability</text>
  <text x="27" y="114" fill="#555555" font-family="'Roboto Mono', monospace" font-size="7">-Perturb</text>
  <text x="40" y="196" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="7.5">RETENTION BENCHMARK: 99.4%</text>

  <!-- Vector Architecture Callouts -->
  <rect x="205" y="38" width="200" height="175" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="215" y="54" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8" font-weight="bold">ARCHITECTURAL MODULES</text>
  <line x1="215" y1="60" x2="395" y2="60" stroke="#222222" stroke-width="1"/>

  <text x="215" y="80" fill="#AAAAAA" font-family="'Roboto Mono', monospace" font-size="7.5">[01] Vector Memory Lattice</text>
  <text x="225" y="94" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7">Non-degrading representation</text>

  <text x="215" y="114" fill="#AAAAAA" font-family="'Roboto Mono', monospace" font-size="7.5">[02] Hysteresis Gate Control</text>
  <text x="225" y="128" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7">Mitigates catastrophic forgetting</text>

  <text x="215" y="148" fill="#AAAAAA" font-family="'Roboto Mono', monospace" font-size="7.5">[03] Stability Invariants</text>
  <text x="225" y="162" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7">Continuous latent verification</text>

  <rect x="215" y="176" width="180" height="26" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="221" y="193" fill="#ff5555" font-family="'Roboto Mono', monospace" font-size="7.5">RESTRICTION: CLOSED B2B ONLY</text>
</svg>'''

with open(os.path.join(out_dir, 'schematic_vorashi.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_vorashi.strip())

# 3. GIOS Technical Architecture Schematic
svg_gios = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 230" width="100%" height="100%" style="background:#050505; border:1px solid #333333; display:block;">
  <defs>
    <pattern id="ggrid" width="15" height="15" patternUnits="userSpaceOnUse">
      <path d="M 15 0 L 0 0 0 15" fill="none" stroke="#0e0e0e" stroke-width="1"/>
    </pattern>
    <marker id="garrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#F5F5DC"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="url(#ggrid)"/>
  <rect x="0" y="0" width="420" height="24" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="10" y="16" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5" letter-spacing="1">FIG 02B // GIOS CAUSAL ENGINE PIPELINE</text>

  <!-- Flowchart Stages -->
  <rect x="15" y="40" width="112" height="38" fill="#000000" stroke="#F5F5DC" stroke-width="1"/>
  <text x="22" y="57" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="7.5" font-weight="bold">STATE MODEL</text>
  <text x="22" y="69" fill="#777777" font-family="'Roboto Mono', monospace" font-size="6.8">Topological Mapping</text>

  <line x1="127" y1="59" x2="151" y2="59" stroke="#F5F5DC" stroke-width="1" marker-end="url(#garrow)"/>

  <rect x="153" y="40" width="115" height="38" fill="#000000" stroke="#F5F5DC" stroke-width="1"/>
  <text x="159" y="57" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="7.5" font-weight="bold">CAUSAL ENGINE</text>
  <text x="159" y="69" fill="#777777" font-family="'Roboto Mono', monospace" font-size="6.8">Hypothesis Inference</text>

  <line x1="268" y1="59" x2="292" y2="59" stroke="#F5F5DC" stroke-width="1" marker-end="url(#garrow)"/>

  <rect x="294" y="40" width="110" height="38" fill="#000000" stroke="#F5F5DC" stroke-width="1"/>
  <text x="300" y="57" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="7.5" font-weight="bold">ROLLOUT DAG</text>
  <text x="300" y="69" fill="#777777" font-family="'Roboto Mono', monospace" font-size="6.8">Predictive Execution</text>

  <!-- Lower Panel: Benchmark Verification -->
  <rect x="15" y="94" width="389" height="118" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="25" y="112" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8" font-weight="bold">OPERATIONAL PIPELINE PARAMETERS</text>
  <line x1="25" y1="118" x2="394" y2="118" stroke="#222222" stroke-width="1"/>

  <text x="25" y="134" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="7.5">+ Search Space Pruning: Novelty delta filtering eliminates brute-force</text>
  <text x="25" y="150" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="7.5">+ Cycle Detection: Multi-period oscillation dampening prevents loops</text>
  <text x="25" y="166" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="7.5">+ Benchmark Proving: ARC-AGI closed-environment abstractions</text>

  <rect x="25" y="178" width="369" height="24" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="31" y="194" fill="#ff5555" font-family="'Roboto Mono', monospace" font-size="7">MANDATE: SUB-LICENSED FOR CLOSED ALGORITHMIC REASONING ONLY</text>
</svg>'''

with open(os.path.join(out_dir, 'schematic_gios.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_gios.strip())

# 4. IDM Technical Architecture Schematic
svg_idm = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 230" width="100%" height="100%" style="background:#050505; border:1px solid #333333; display:block;">
  <defs>
    <pattern id="igrid" width="15" height="15" patternUnits="userSpaceOnUse">
      <path d="M 15 0 L 0 0 0 15" fill="none" stroke="#0e0e0e" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#igrid)"/>
  <rect x="0" y="0" width="420" height="24" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="10" y="16" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5" letter-spacing="1">FIG 02C // IDM (APPLIED) PRE-GEOMETRIC COMPUTE</text>

  <!-- Lattice Graph Graphic -->
  <rect x="15" y="38" width="185" height="175" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="23" y="54" fill="#888888" font-family="'Roboto Mono', monospace" font-size="7.5">EMERGENT STATE LATTICE</text>
  
  <!-- Node matrix -->
  <circle cx="45" cy="80" r="3" fill="#F5F5DC"/>
  <circle cx="95" cy="75" r="4" fill="#F5F5DC"/>
  <circle cx="155" cy="85" r="3" fill="#F5F5DC"/>
  <circle cx="65" cy="120" r="4" fill="#F5F5DC"/>
  <circle cx="120" cy="115" r="5" fill="#F5F5DC"/>
  <circle cx="170" cy="125" r="3" fill="#F5F5DC"/>
  <circle cx="45" cy="165" r="3" fill="#F5F5DC"/>
  <circle cx="105" cy="160" r="4" fill="#F5F5DC"/>
  <circle cx="155" cy="170" r="3" fill="#F5F5DC"/>

  <line x1="45" y1="80" x2="95" y2="75" stroke="#444444" stroke-width="1"/>
  <line x1="95" y1="75" x2="155" y2="85" stroke="#444444" stroke-width="1"/>
  <line x1="45" y1="80" x2="65" y2="120" stroke="#444444" stroke-width="1"/>
  <line x1="95" y1="75" x2="120" y2="115" stroke="#F5F5DC" stroke-width="1.5"/>
  <line x1="155" y1="85" x2="170" y2="125" stroke="#444444" stroke-width="1"/>
  <line x1="65" y1="120" x2="120" y2="115" stroke="#F5F5DC" stroke-width="1.5"/>
  <line x1="120" y1="115" x2="170" y2="125" stroke="#444444" stroke-width="1"/>
  <line x1="65" y1="120" x2="45" y2="165" stroke="#444444" stroke-width="1"/>
  <line x1="120" y1="115" x2="105" y2="160" stroke="#F5F5DC" stroke-width="1.5"/>
  <line x1="170" y1="125" x2="155" y2="170" stroke="#444444" stroke-width="1"/>
  <line x1="45" y1="165" x2="105" y2="160" stroke="#444444" stroke-width="1"/>
  <line x1="105" y1="160" x2="155" y2="170" stroke="#444444" stroke-width="1"/>

  <text x="23" y="196" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="7">D-OPERATOR DISTURBANCE: STABLE</text>

  <!-- Description Panel -->
  <rect x="210" y="38" width="195" height="175" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="220" y="54" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8" font-weight="bold">COMPUTATIONAL SCOPE</text>
  <line x1="220" y1="60" x2="395" y2="60" stroke="#222222" stroke-width="1"/>

  <text x="220" y="80" fill="#AAAAAA" font-family="'Roboto Mono', monospace" font-size="7.5">[01] Pre-Geometric Calculus</text>
  <text x="228" y="94" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7">Discrete optimal transport</text>

  <text x="220" y="114" fill="#AAAAAA" font-family="'Roboto Mono', monospace" font-size="7.5">[02] Spacetime Emergence</text>
  <text x="228" y="128" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7">Mathematical field modeling</text>

  <text x="220" y="148" fill="#AAAAAA" font-family="'Roboto Mono', monospace" font-size="7.5">[03] Advanced Simulations</text>
  <text x="228" y="162" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7">Non-standard compute matrices</text>

  <rect x="220" y="176" width="175" height="26" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="226" y="193" fill="#ff5555" font-family="'Roboto Mono', monospace" font-size="7.2" font-weight="bold">[STRICT FIELD RESTRICTION]</text>
</svg>'''

with open(os.path.join(out_dir, 'schematic_idm.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_idm.strip())

# 5. Compliance Protocol Workflow Schematic
svg_flow = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 130" width="100%" height="100%" style="background:#050505; border:1px solid #333333; display:block;">
  <defs>
    <marker id="farrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#F5F5DC"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="920" height="24" fill="#0d0d0d" stroke="#222222" stroke-width="1"/>
  <text x="12" y="16" fill="#888888" font-family="'Roboto Mono', monospace" font-size="8.5" letter-spacing="1">FIG 03 // STATUTORY INTAKE AND AUDIT ADJUDICATION FUNNEL (FORM CA-01)</text>

  <!-- 4 Step Boxes -->
  <!-- Box 1 -->
  <rect x="20" y="38" width="195" height="78" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="30" y="56" fill="#888888" font-family="'Roboto Mono', monospace" font-size="7.5">PHASE 01</text>
  <text x="30" y="72" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="bold">CREDENTIAL INTAKE</text>
  <text x="30" y="88" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7.5">Entity filings and beneficial</text>
  <text x="30" y="100" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7.5">ownership verification (&gt;=25%)</text>

  <line x1="215" y1="77" x2="245" y2="77" stroke="#F5F5DC" stroke-width="1" marker-end="url(#farrow)"/>

  <!-- Box 2 -->
  <rect x="250" y="38" width="195" height="78" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="260" y="56" fill="#888888" font-family="'Roboto Mono', monospace" font-size="7.5">PHASE 02</text>
  <text x="260" y="72" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="bold">CA-FORM-01 AUDIT</text>
  <text x="260" y="88" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7.5">12-point statutory audit</text>
  <text x="260" y="100" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7.5">Field-of-use screening</text>

  <line x1="445" y1="77" x2="475" y2="77" stroke="#F5F5DC" stroke-width="1" marker-end="url(#farrow)"/>

  <!-- Box 3 -->
  <rect x="480" y="38" width="195" height="78" fill="#000000" stroke="#333333" stroke-width="1"/>
  <text x="490" y="56" fill="#888888" font-family="'Roboto Mono', monospace" font-size="7.5">PHASE 03</text>
  <text x="490" y="72" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="bold">CTO / CLO EXECUTION</text>
  <text x="490" y="88" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7.5">Mandatory C-level attestation</text>
  <text x="490" y="100" fill="#666666" font-family="'Roboto Mono', monospace" font-size="7.5">Grant-back covenant binding</text>

  <line x1="675" y1="77" x2="705" y2="77" stroke="#F5F5DC" stroke-width="1" marker-end="url(#farrow)"/>

  <!-- Box 4 -->
  <rect x="710" y="38" width="190" height="78" fill="#000000" stroke="#F5F5DC" stroke-width="1.5"/>
  <text x="720" y="56" fill="#888888" font-family="'Roboto Mono', monospace" font-size="7.5">PHASE 04</text>
  <text x="720" y="72" fill="#F5F5DC" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="bold">DEPLOY AND AUDIT</text>
  <text x="720" y="88" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="7.5">Sandboxed runtime keys</text>
  <text x="720" y="100" fill="#CCCCCC" font-family="'Roboto Mono', monospace" font-size="7.5">Unannounced bi-annual audits</text>
</svg>'''

with open(os.path.join(out_dir, 'schematic_compliance_flow.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_flow.strip())

print('All 5 technical schematics created successfully.')
