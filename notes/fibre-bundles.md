# Fibre Bundles, Connections & Characteristic Classes — A Complete Study Note

*Based on Nakahara, "Geometry, Topology and Physics," Chapters 9, 10 & 11*

This note has three parts. **Part I** (Chapter 9) builds the static stage: what a fibre bundle is and how its twisting is encoded in transition functions. **Part II** (Chapter 10) puts dynamics on that stage: a *connection* tells you how to move/compare/differentiate things as you travel along the base, and its curvature is exactly the Yang–Mills field strength of gauge theory. **Part III** (Chapter 11) explains why the curvature integrals that keep appearing in Part II (monopole charge, instanton number) are always quantized, connection-independent topological invariants — and builds the whole catalogue of such invariants (Chern, Pontryagin, Euler, Todd, and Stiefel–Whitney classes).

---
---

# PART I — Fibre Bundles (Chapter 9)

## 0. The Big Picture 

A **manifold** looks locally like $\mathbb{R}^m$ but can be globally curved or twisted. A **fibre bundle** pushes this idea one level higher: it is a space that *looks locally* like a **product** of two spaces, $\text{base} \times \text{fibre}$, but globally may be **twisted** so that it is *not* a genuine product.

The whole chapter is an extended answer to one question:

> **How do you glue together local product pieces $U_i \times F$ into a single global object, and how much twisting can the gluing introduce?**

The twisting is encoded entirely in the **transition functions** $t_{ij}$. This single idea unifies everything: tangent vectors, gauge fields, spinors, monopoles, and instantons are all sections of suitable bundles, and their topological "charge" is the obstruction to untwisting the bundle.

The canonical mental image to keep throughout:

- **Cylinder** = trivial bundle (no twist), structure group trivial.
- **Möbius strip** = nontrivial bundle (one twist), structure group $\mathbb{Z}_2$.

Both are bundles over the circle $S^1$ with fibre an interval. They differ *only* in their transition function.

---

## 1. Motivating Example: The Tangent Bundle

### 1.1 Definition

Given an $m$-dimensional manifold $M$, the **tangent bundle** collects all tangent spaces:

$$TM \equiv \bigcup_{p \in M} T_pM.$$

- $M$ is the **base space**.
- Each $T_pM \cong \mathbb{R}^m$ is the **fibre at $p$**.
- A point of $TM$ is a pair (point $p$, vector $V$ sitting at $p$).

### 1.2 Local triviality

Over a chart $U_i$ with coordinates $x^\mu = \varphi_i(p)$, an element of

$$TU_i \equiv \bigcup_{p \in U_i} T_pM$$

is specified by $(p, V)$ where $V = V^\mu(p)\,\partial/\partial x^\mu|_p$. Since $U_i \cong \mathbb{R}^m$ and $T_pM \cong \mathbb{R}^m$, the piece $TU_i$ looks like the product $\mathbb{R}^m \times \mathbb{R}^m$. So **locally** the tangent bundle is just a product $U_i \times \mathbb{R}^m$. It is a $2m$-dimensional manifold.

### 1.3 Projection

The **projection** $\pi: TU_i \to U_i$ throws away the vector and keeps only the base point: $\pi(u) = p$. The inverse image $\pi^{-1}(p) = T_pM$ is exactly the fibre. The projection is defined **globally** (it does not depend on a choice of chart).

### 1.4 Where the twisting hides: changing charts

If $M = \mathbb{R}^m$, then $TM = \mathbb{R}^m \times \mathbb{R}^m$ globally — boring, trivial. For a general $M$ the bundle is **not** a global product, and this nontriviality measures the topological nontriviality of $M$.

To see the twist you must compare **two overlapping charts** $U_i, U_j$. The same vector $V$ has two coordinate presentations:

$$V = V^\mu \frac{\partial}{\partial x^\mu}\Big|_p = \tilde V^\mu \frac{\partial}{\partial y^\mu}\Big|_p,$$

related by the Jacobian:

$$\boxed{\tilde V^\nu = \frac{\partial y^\nu}{\partial x^\mu}(p)\, V^\mu.}$$

The matrix $G^\nu{}_\mu \equiv \partial y^\nu/\partial x^\mu$ must be non-singular, i.e. it lives in $GL(m, \mathbb{R})$. So **whenever you change charts, the fibre coordinates get rotated by an element of $GL(m,\mathbb{R})$**. This group is the **structure group** of $TM$.

> **Key takeaway:** The fibres are "interwoven" by $GL(m,\mathbb{R})$-valued transition rules. That interweaving is the source of all topological complexity.

---

## 2. Fibre Bundles in General

### 2.1 The formal definition

A **(differentiable) fibre bundle** $(E, \pi, M, F, G)$ consists of:

| Ingredient | Symbol | Role |
|---|---|---|
| Total space | $E$ | the whole twisted object |
| Base space | $M$ | what you project down to |
| Fibre (typical fibre) | $F$ | the "vertical" model space |
| Projection | $\pi: E \to M$ | surjection; $\pi^{-1}(p) = F_p \cong F$ |
| Structure group | $G$ (a Lie group) | acts on $F$ on the **left**; encodes allowed twists |
| Open cover + local trivializations | $\{U_i\}$, $\phi_i$ | diffeomorphisms $\phi_i: U_i \times F \to \pi^{-1}(U_i)$ |
| Transition functions | $t_{ij}: U_i \cap U_j \to G$ | glue overlapping pieces |

**Local trivialization** $\phi_i: U_i \times F \to \pi^{-1}(U_i)$ satisfies $\pi \circ \phi_i(p,f) = p$. Reading it backwards, $\phi_i^{-1}$ shows that $\pi^{-1}(U_i)$ really is a product $U_i \times F$.

Writing $\phi_{i,p}(f) \equiv \phi_i(p,f)$, the **transition function** on an overlap is

$$t_{ij}(p) \equiv \phi_{i,p}^{-1} \circ \phi_{j,p} : F \to F, \qquad t_{ij}(p) \in G,$$

and the two trivializations are related by

$$\boxed{\phi_j(p,f) = \phi_i\big(p,\ t_{ij}(p)\,f\big).}$$

Shorthand: write $E \xrightarrow{\pi} M$ or just $E$.

### 2.2 Consistency (cocycle) conditions

For the gluing to be globally consistent, the transition functions must satisfy:

$$
\begin{aligned}
t_{ii}(p) &= \text{identity} && (p \in U_i) \\
t_{ij}(p) &= t_{ji}(p)^{-1} && (p \in U_i \cap U_j) \\
t_{ij}(p)\, t_{jk}(p) &= t_{ik}(p) && (p \in U_i \cap U_j \cap U_k)
\end{aligned}
$$

The third one (the **cocycle condition**) is the important one — it is exactly what lets local pieces be glued without contradiction on triple overlaps.

> **Trivial bundle:** if *all* $t_{ij}$ can be chosen to be the identity, the bundle is trivial and equals the global product $M \times F$.

### 2.3 Non-uniqueness and gauge freedom

The transition functions are *not* unique. If $\{\phi_i\}$ and $\{\tilde\phi_i\}$ describe the same bundle, define the within-chart change $g_i(p) \equiv \phi_{i,p}^{-1} \circ \tilde\phi_{i,p} \in G$. Then

$$\boxed{\tilde t_{ij}(p) = g_i(p)^{-1}\, t_{ij}(p)\, g_j(p).}$$

**Physics dictionary:** $t_{ij}$ are the gauge transformations needed to paste charts together; $g_i$ are the **gauge degrees of freedom within a chart**. This formula is precisely a gauge transformation of the "transition gauge field." If the bundle is trivial you may set all $t_{ij}=$ identity, and then the most general transition function takes the pure-gauge form $t_{ij}(p) = g_i(p)^{-1} g_j(p)$.

### 2.4 Sections

A **section** (cross section) is a smooth map $s: M \to E$ with $\pi \circ s = \text{id}_M$ — i.e. it picks one point in each fibre, smoothly. The set is denoted $\Gamma(M, F)$.

- A **local section** is only defined on some $U \subset M$.
- Example: $\Gamma(M, TM) = \mathfrak{X}(M)$, the **vector fields** on $M$.
- **Crucial fact:** not every bundle admits a **global** section. (Vector bundles always admit the trivial *null* section, but that's special — see §9 below.)

### 2.5 Worked example: cylinder vs Möbius strip

Bundle over $S^1$, fibre $F = [-1,1]$. Cover $S^1$ with $U_1 = (0,2\pi)$, $U_2 = (-\pi,\pi)$; the overlap has two components $A=(0,\pi)$ and $B=(\pi,2\pi)$.

On $A$, set $t_{12} = $ identity. On $B$ there are two choices:

- **(I)** $t_{12} = $ identity $\Rightarrow$ **cylinder**, structure group $G = \{e\}$ (trivial bundle $S^1 \times F$).
- **(II)** $t_{12}: t \mapsto -t \Rightarrow$ **Möbius strip**, structure group $G = \{e,g\}$ with $g: t\mapsto -t$. Since $g^2 = e$, we get $G \cong \mathbb{Z}_2$.

> *Remark:* $\mathbb{Z}_2$ is not a Lie group — this is the **one** place a discrete structure group appears.

This example is the entire chapter in miniature: same base, same fibre, different transition function on one overlap component $\Rightarrow$ globally different bundles.

---

## 3. Constructions on Bundles

### 3.1 Reconstruction (the "minimal data" theorem)

**Claim:** Given $M$, a cover $\{U_i\}$, transition functions $t_{ij}$, the fibre $F$, and the group $G$ (satisfying the cocycle conditions), you can **reconstruct the bundle uniquely**.

Recipe: start from the disjoint union $X \equiv \bigsqcup_i U_i \times F$, then glue with the equivalence relation

$$(p,f) \sim (q,f') \iff p = q \text{ and } f' = t_{ij}(p) f.$$

Define $E = X/\!\sim$, projection $\pi:[(p,f)] \mapsto p$, and trivializations $\phi_i:(p,f)\mapsto[(p,f)]$. This is the practical "build a bundle from gluing data" procedure used constantly in physics.

### 3.2 Bundle maps

A smooth map $\bar f: E' \to E$ is a **bundle map** if it sends whole fibres to whole fibres, i.e. it induces a well-defined map $f: M' \to M$ on the base making the square commute:

$$
\begin{array}{ccc}
E' & \xrightarrow{\ \bar f\ } & E \\
{\scriptstyle \pi'}\downarrow & & \downarrow{\scriptstyle \pi}\\
M' & \xrightarrow{\ f\ } & M
\end{array}
$$

*Caution:* a generic smooth map $E' \to E$ is **not** a bundle map — it may scatter points of one fibre across different fibres.

### 3.3 Equivalent bundles

$E'$ and $E$ over the **same** base $M$ are **equivalent** if there is a bundle map $\bar f: E' \to E$ that is a diffeomorphism and induces $f = \text{id}_M$. Intuitively: same bundle, possibly described with different trivializations.

### 3.4 Pullback bundles

Given $E \xrightarrow{\pi} M$ and a map $f: N \to M$, the **pullback** $f^*E$ is a new bundle over $N$ with the same fibre $F$:

$$f^*E \equiv \{(p,u) \in N \times E \mid f(p) = \pi(u)\}.$$

Its fibre over $p \in N$ is a copy of the fibre $F_{f(p)}$ over $f(p) \in M$. Projections $\pi_1:(p,u)\mapsto p$ and $\pi_2:(p,u)\mapsto u$ fit into a commuting square. The transition functions simply **pull back**:

$$\boxed{t^*_{ij}(p) = t_{ij}(f(p)).}$$

If $N=M$ and $f=\text{id}$, then $f^*E$ and $E$ are equivalent.

### 3.5 Homotopy axiom and a powerful corollary

**Theorem (Homotopy axiom).** If $f, g: N \to M$ are **homotopic**, then $f^*E$ and $g^*E$ are equivalent bundles over $N$.

**Consequence (Corollary 9.1).** *If $M$ is contractible to a point, every bundle over $M$ is trivial.*

Sketch: contractibility gives a homotopy $F(p,0)=p$, $F(p,1)=p_0$. Pulling back along $h_0=\text{id}$ gives $E$ itself; pulling back along $h_1=$ const gives the trivial bundle $\{p_0\}\times F \Rightarrow M \times F$. Homotopy makes these equivalent, so $E$ is trivial. (E.g. $T\mathbb{R}^m$ is trivial.)

> **Why this matters:** nontrivial bundles can only live over **topologically nontrivial** bases (spheres, tori, etc.). All the interesting physics — monopoles, instantons — needs a base with nontrivial topology.

---

## 4. Vector Bundles

### 4.1 Definition

A **vector bundle** is a fibre bundle whose fibre is a **vector space**, $F = \mathbb{R}^k$ (or $\mathbb{C}^k$).

- $k$ = **fibre dimension**, denoted $\dim E$ (even though the total space has dimension $m+k$).
- Structure group is $GL(k,\mathbb{R})$ (or $GL(k,\mathbb{C})$), because transition functions must be linear isomorphisms of the fibre.

### 4.2 Examples

- **Tangent bundle $TM$:** fibre $\mathbb{R}^m$, structure group $GL(m,\mathbb{R})$, transition $G^\mu{}_\nu = (\partial x^\mu/\partial y^\nu)$. Sections = vector fields, $\mathfrak{X}(M)=\Gamma(M,TM)$.
  - Worked case $TS^2$: with the two stereographic charts $U_N, U_S$, the transition function is a rotation by $2\theta$ (plus a rescaling), $t_{SN} = \frac{1}{r^2}\begin{pmatrix} -\cos 2\theta & -\sin 2\theta \\ \sin 2\theta & -\cos 2\theta\end{pmatrix}$, with $t_{NS}=t_{SN}^{-1}$.
- **Normal bundle $NM$:** for $M$ embedded in $\mathbb{R}^{m+k}$, the fibre $N_pM$ is the orthogonal complement of $T_pM$; fibre $\cong \mathbb{R}^k$. For $S^2 \subset \mathbb{R}^3$, $NS^2$ is trivial: $S^2 \times \mathbb{R}$.
- **Line bundle:** fibre is 1-dimensional. Cylinder = trivial $\mathbb{R}$-line bundle; Möbius strip = nontrivial real line bundle. Structure group $GL(1,\mathbb{R}) = \mathbb{R}\setminus\{0\}$ (Abelian).
- **Canonical line bundle $L$ over $\mathbb{C}P^n$:** the fibre over a point $p$ (which *is* a complex line in $\mathbb{C}^{n+1}$) is that very line. $L \equiv \{(p,v) \mid v = ap,\ a\in\mathbb{C}\}$.
- **QM wavefunction:** $\psi(x)$ is a section of a (trivial) complex line bundle $L = \mathbb{R}^3 \times \mathbb{C}$. Around a magnetic monopole the relevant line bundle over $S^2$ becomes nontrivial.

### 4.3 Frames

On $TM$ each fibre has the natural basis $\{\partial/\partial x^\mu\}$ (or an orthonormal basis $\{\hat e_\alpha\}$ if there's a metric). More generally, on a chart $U_i$ of a vector bundle you can choose $k$ linearly independent sections $\{e_1(p),\dots,e_k(p)\}$ — a **frame** over $U_i$. A frame gives the trivialization $\phi_i^{-1}(V) = (p, \{V^\alpha(p)\})$ where $V = V^\alpha e_\alpha(p)$.

Under a change of frame $\tilde e_\beta(p) = e_\alpha(p) G(p)^\alpha{}_\beta$, components transform inversely:

$$\tilde V^\beta = G^{-1}(p)^\beta{}_\alpha V^\alpha,$$

so the transition function is the matrix $G^{-1}(p)$. (Basis vectors and components transform oppositely — the usual covariant/contravariant story.)

### 4.4 Cotangent and dual bundles

The **cotangent bundle** $T^*M = \bigcup_p T^*_pM$ has fibre basis $\{dx^\mu\}$ dual to $\{\partial/\partial x^\mu\}$. One-forms transform with the inverse Jacobian:

$$\tilde\omega_\mu = G_\mu{}^\nu(p)\,\omega_\nu,\qquad G_\mu{}^\nu = (\partial x^\nu/\partial y^\mu).$$

Sections are 1-forms: $\Gamma(M,T^*M)=\Omega^1(M)$. More generally any vector bundle $E$ has a **dual bundle** $E^*$ whose fibre is the space of linear maps $F\to\mathbb{R}$ (or $\mathbb{C}$), with dual basis $\langle\theta^\alpha(p), e_\beta(p)\rangle = \delta^\alpha{}_\beta$.

### 4.5 Sections, fibre metric, the null section

Sections of a vector bundle add and scale pointwise:
$(s+s')(p)=s(p)+s'(p)$, $(fs)(p)=f(p)s(p)$ for $f \in \mathcal{F}(M)$.

Every vector bundle admits the **null section** $s_0$ (zero vector in each fibre) — always global. A **fibre metric** $h_{\mu\nu}(p)$ defines pointwise inner products of sections (with a complex conjugate in the $\mathbb{C}^k$ case).

### 4.6 Product bundle and Whitney sum (the "fibrewise direct sum")

- **Product bundle** $E \times E' \to M \times M'$: fibre $F \oplus F'$, over a *product* base.
- **Whitney sum** $E \oplus E'$ over the **same** base $M$: it is the pullback of $E \times E'$ by the diagonal $f(p)=(p,p)$. Its fibre over $p$ is $F_p \oplus F'_p$. The transition functions are **block diagonal**:

$$T_{ij}(p) = \begin{pmatrix} t^E_{ij}(p) & 0 \\ 0 & t^{E'}_{ij}(p)\end{pmatrix}.$$

**Example.** $TS^2 \oplus NS^2$ (with $S^2 \subset \mathbb{R}^3$) is **trivial** over $S^2$, fibre $\cong \mathbb{R}^3$. This is the prototype: a nontrivial bundle ($TS^2$) plus a complementary bundle can sum to something trivial — the basis of $K$-theory intuition.

(There is also a tensor product $\otimes$, distributive over $\oplus$ — Exercise 9.1.)

---

## 5. Principal Bundles

### 5.1 Definition

A **principal bundle** $P(M,G)$ is a fibre bundle whose **fibre is the structure group $G$ itself**, $F = G$.

Because the fibre is a group, there's a natural **right action** of $G$ on $P$, defined chart-by-chart by $\phi_i^{-1}(ua) = (p, g_i a)$, i.e.

$$ua = \phi_i(p, g_i a).$$

Key properties of this right action:

- **Well defined** (independent of trivialization), because right multiplication commutes with the left action of the transition functions.
- **Fibre-preserving:** $\pi(ua) = \pi(u)$.
- **Transitive** on each fibre: any $u_1,u_2$ in the same fibre are related by some $a\in G$.
- **Free:** $ua = u \Rightarrow a = e$.

So each fibre $\pi^{-1}(p)$ is diffeomorphic to $G$, and you can sweep out the whole fibre as $\{ua \mid a\in G\}$.

### 5.2 Canonical local trivialization from a section

Given a local section $s_i(p)$ over $U_i$, every $u$ in the fibre is uniquely $u = s_i(p) g_u$. Define $\phi_i^{-1}(u) = (p, g_u)$. Then the section is $s_i(p) = \phi_i(p, e)$ and $\phi_i(p,g) = s_i(p)g$. On overlaps, two such sections relate by the transition function (note the right action):

$$\boxed{s_i(p) = s_j(p)\, t_{ji}(p).}$$

### 5.3 The physics: gauge theory lives here

| Bundle language | Gauge-theory language |
|---|---|
| Structure group $G$ | gauge group |
| Right action of $G$ | gauge transformation |
| Transition function $t_{ij}$ | gauge transformation between patches |
| Section of $P$ | a choice of gauge |
| (Chapter 10) connection | gauge potential $A_\mu$ |

### 5.4 Example: magnetic monopole = $U(1)$ bundle over $S^2$

Cover $S^2$ by northern/southern caps $U_N, U_S$ overlapping near the equator. With $\phi_N^{-1}(u) = (p, e^{i\alpha_N})$, $\phi_S^{-1}(u)=(p,e^{i\alpha_S})$, take a transition function $t_{NS} = e^{in\phi}$. **Single-valuedness on the equator forces $n \in \mathbb{Z}$.** The fibre coordinates relate by

$$e^{i\alpha_N} = e^{in\phi}\,e^{i\alpha_S}.$$

- $n=0$: trivial bundle $P_0 = S^2 \times S^1$.
- $n\neq 0$: twisted $U(1)$ bundle $P_n$.

The integer $n$ is the element of $\pi_1(U(1)) = \mathbb{Z}$ — it is the **quantized magnetic charge**. The remarkable lesson: *the topology of the bundle is labelled by an integer*. Since $U(1)$ is Abelian, left and right actions coincide; the right action is exactly the $U(1)$ gauge transformation.

### 5.5 Example: instanton = $SU(2)$ bundle over $S^4$

Compactify $\mathbb{R}^4$ to $S^4 = \mathbb{R}^4 \cup \{\infty\}$. Cover by $U_N$ (a ball) and $U_S$ (its complement); the overlap is essentially $S^3$. The transition function maps $S^3 \to SU(2)$, classified by

$$\pi_3(SU(2)) = \mathbb{Z}.$$

This integer is the **instanton number**. Using $SU(2) \cong S^3$, the class-1 transition function is

$$t_{NS}(p) = \frac{1}{R}\Big(t\,I_2 + i\textstyle\sum_i x^i \sigma_i\Big),\qquad R = (t^2+\textstyle\sum_i (x^i)^2)^{1/2},$$

and the class-$n$ one is its $n$-th power. As $(t,\mathbf{x})$ covers $S^3$ once, $t_{NS}$ wraps $SU(2)$ once $\Rightarrow$ homotopy class 1.

### 5.6 Hopf maps (bundles where the total space is a sphere)

- **$S^3 \xrightarrow{\pi} S^2$**, fibre $U(1)=S^1$. Write $S^3 = \{|z^0|^2+|z^1|^2=1\}$; the Hopf map sends $(z^0,z^1) \mapsto$ its complex line, i.e. $\mathbb{C}P^1 = S^2$. Transition function on the equator $t_{NS} = z^0/z^1$ (unit modulus), wrapping the circle once $\Rightarrow$ class 1 of $\pi_1(U(1))=\mathbb{Z}$. **A unit magnetic monopole is exactly this Hopf bundle.**
- **$S^7 \xrightarrow{\pi} S^4$**, fibre $S^3 = SU(2)$ (via quaternions). Class 1 of $\pi_3(SU(2))=\mathbb{Z}$. **A unit instanton is this Hopf map.**
- **$S^{15}\to S^8$**, fibre $S^7$ (via octonions) — but $S^7$ is *not* a group (octonion multiplication is non-associative), so this is not a principal bundle; no known physics use.

### 5.7 Example: coset spaces $G \to G/H$

If $H$ is a closed Lie subgroup of $G$, then $G$ is a principal bundle with fibre $H$ over base $M = G/H$. The right action is $g\mapsto ga$, projection $\pi: g\mapsto [g]=\{gh\}$. Useful identities:

$$O(n)/O(n-1) = S^{n-1},\qquad U(n)/U(n-1) = S^{2n-1}.$$

---

## 6. Associated Bundles

Given a principal bundle $P(M,G)$ and a left action of $G$ on a manifold $F$, build the **associated bundle** by identifying

$$(u,f) \sim (ug, g^{-1}f).$$

The associated bundle is $E = P \times F / G$.

**Associated vector bundle** $P \times_\rho V$: take $F = V$ a $k$-dim vector space and $\rho$ a representation of $G$. Identify $(u,v)\sim(ug, \rho(g)^{-1}v)$. Its transition functions are $\rho(t_{ij}(p))$ — the *same* transition data as $P$, just run through the representation $\rho$.

**Converse:** any vector bundle $E$ induces a principal bundle $P(E)$ with structure group $GL(k,\mathbb{R})$ (or $\mathbb{C}$) by reusing $E$'s transition functions.

> **Punchline:** $E$ and $P(E)$ share the same transition functions, hence the **same twisting**. The vector bundle and its principal bundle carry identical topological information.

### 6.1 The frame bundle $LM$

The principal bundle associated with $TM$ is the **frame bundle** $LM = \bigcup_p L_pM$, where $L_pM$ is the set of frames (ordered bases) at $p$. Structure group $GL(m,\mathbb{R})$ acting on frames by $Y_\beta = X_\alpha a^\alpha{}_\beta$. Transition functions are the Jacobians $t^L_{ij}(p) = (\partial x^\mu/\partial y^\nu)_p$ — again identical to $TM$'s.

**In GR:** right action = local Lorentz transformation; left action = general coordinate transformation. If frames are orthonormalized by a metric, $(X^\mu{}_\alpha)$ becomes the **vierbein** and the group reduces to $O(m)$.

### 6.2 Spin bundles

$GL(k,\mathbb{R})$ has no spinor representation, so to define spinors you start from the **orthonormal frame bundle** with group $SO(k)$ and try to lift it to its universal cover $\text{SPIN}(k)$. This lift may be **obstructed** (discussed in §11.6 of the book).

For 4D Lorentzian $M$: structure group reduces to $O^+_\uparrow(3,1)$, universally covered $2{:}1$ by $SL(2,\mathbb{C})$. Then:

- **Weyl spinor:** section of $(W,\pi,M,\mathbb{C}^2, SL(2,\mathbb{C}))$ — the $(1/2,0)$ representation.
- **Dirac spinor:** section of $(D,\pi,M,\mathbb{C}^4, SL(2,\mathbb{C})\oplus\overline{SL(2,\mathbb{C})})$ — belongs to $(1/2,0)\oplus(0,1/2)$.

---

## 7. Triviality of Bundles

A bundle is **trivial** if it equals the direct product $M\times F$.

**Theorem 9.2.** *A principal bundle is trivial if and only if it admits a global section.*

*Proof idea.* A global section $s$ lets you write every point uniquely as $u = s(p)a$ (using transitivity + freeness of the right action). The map $\Phi: s(p)a \mapsto (p,a)$ is a diffeomorphism $P \cong M\times G$. Conversely, a trivialization gives a global section by fixing $g$: $s_g(p)=\phi(p,g)$. $\square$

> This is why principal bundles are so useful: **triviality $\Leftrightarrow$ existence of a global gauge.** A monopole/instanton being nontrivial means *no single global gauge exists* — you genuinely need patched gauge potentials (Dirac/Wu–Yang construction).

**Corollary 9.2.** A vector bundle $E$ is trivial **iff** its associated principal bundle $P(E)$ admits a global section. (You can't use Theorem 9.2 directly on $E$ because vector bundles *always* have the null section — that's why you pass to $P(E)$.)

---

## 8. The Single Most Important Idea, Restated

Everything reduces to **transition functions valued in the structure group**, modulo the gauge equivalence $\tilde t_{ij} = g_i^{-1} t_{ij} g_j$. The topological "charge" of a bundle is **how the transition functions wrap around the overlaps**, measured by a homotopy group:

| Physical object | Bundle | Base | Group $G$ | Overlap | Classified by |
|---|---|---|---|---|---|
| Möbius strip | line bundle | $S^1$ | $\mathbb{Z}_2$ | 2 points | $\mathbb{Z}_2$ |
| Magnetic monopole | $U(1)$ principal | $S^2$ | $U(1)$ | $\sim S^1$ | $\pi_1(U(1))=\mathbb{Z}$ |
| Instanton | $SU(2)$ principal | $S^4$ | $SU(2)$ | $\sim S^3$ | $\pi_3(SU(2))=\mathbb{Z}$ |

The pattern: **a bundle over $S^n$ built from two patches is classified by $\pi_{n-1}(G)$**, because the gluing happens on the equatorial $S^{n-1}$.

---

## 9. Glossary (quick reference)

- **Total space $E$** — the full twisted bundle.
- **Base $M$** — what you project onto.
- **Fibre $F$** — the model "vertical" space; $\pi^{-1}(p)\cong F$.
- **Projection $\pi$** — forgets the fibre coordinate.
- **Structure group $G$** — Lie group of allowed fibre transformations; acts on $F$ on the left.
- **Local trivialization $\phi_i$** — diffeomorphism $U_i\times F \cong \pi^{-1}(U_i)$.
- **Transition function $t_{ij}$** — $G$-valued gluing map on overlaps; satisfies cocycle conditions.
- **Section** — smooth right-inverse of $\pi$; "one point per fibre."
- **Trivial bundle** — $E = M\times F$; equivalently all $t_{ij}=$ id; equivalently (principal case) admits a global section.
- **Vector bundle** — fibre is a vector space; $G \subset GL(k)$.
- **Principal bundle** — fibre *is* the group $G$.
- **Associated bundle** — built from a principal bundle + a $G$-action on a new fibre; same transition data.
- **Pullback $f^*E$** — bundle over $N$ from $E$ over $M$ via $f:N\to M$; $t^*_{ij}=t_{ij}\circ f$.
- **Whitney sum $E\oplus E'$** — fibrewise direct sum; block-diagonal transition functions.


---
---

# PART II — Connections on Fibre Bundles (Chapter 10)

## 0. The Big Picture 

Chapter 9 built bundles but left them "static" — no way to compare a fibre at one point with the fibre at a nearby point. A **connection** fixes that: it is a rule for splitting, at every point $u$ of the total space, the tangent space $T_uP$ into a **vertical** part (motion *within* the fibre) and a **horizontal** part (motion that constitutes "moving without twisting" along the base).

The whole chapter is the working-out of one slogan:

> **A connection on a principal bundle $\Leftrightarrow$ a $\mathfrak{g}$-valued one-form $\omega$ (the gauge potential) $\Leftrightarrow$ a rule for parallel transport $\Leftrightarrow$ a covariant derivative on every associated bundle.**

Its curvature $\Omega = D\omega$ is, in local coordinates, exactly the **Yang–Mills field strength** $F_{\mu\nu}$. Everything downstream — Maxwell's equations, the Dirac monopole, the Aharonov–Bohm effect, Yang–Mills theory, instantons, Berry's phase — is one specialization or another of this single geometric object.

| Geometry | Physics |
|---|---|
| Connection one-form $\omega$ on $P$ | — (globally defined, gauge-independent) |
| Local form $\mathcal{A}_i = \sigma_i^*\omega$ | gauge potential $A_\mu$ (up to a factor of $i$) |
| Curvature $\Omega = D\omega$ | — (globally defined) |
| Local form $\mathcal{F} = \sigma^*\Omega$ | Yang–Mills field strength $F_{\mu\nu}$ |
| Horizontal lift of a curve | parallel transport |
| Holonomy of a loop | Wilson loop / Berry's phase / Aharonov–Bohm phase |
| Transition function $t_{ij}$ acting on $\mathcal{A}_i$ | gauge transformation |

---

## 1. Connections on Principal Bundles

### 1.1 Vertical and horizontal subspaces

Let $P(M,G)$ be a principal bundle, $u \in P$ with $\pi(u) = p$. The fibre through $u$ is $G_p \cong G$.

**Vertical subspace $V_uP$.** For $A \in \mathfrak{g}$, the curve $t \mapsto u\exp(tA)$ stays inside the fibre $G_p$ (since $\pi(u\exp(tA)) = \pi(u) = p$). Its tangent vector at $t=0$ defines the **fundamental vector field** $A^\#$:

$$A^\# f(u) = \frac{d}{dt} f(u\exp(tA))\Big|_{t=0}.$$

This gives a vector space isomorphism $\sharp: \mathfrak{g} \to V_uP$, and it **preserves the Lie bracket**: $[A^\#, B^\#] = [A,B]^\#$ (Exercise 10.1). Also $\pi_* X = 0$ for any $X \in V_uP$ — vertical vectors are invisible to the base.

**Horizontal subspace $H_uP$** is a *complement* of $V_uP$ in $T_uP$ — but which complement is exactly what a connection chooses.

### 1.2 Definition 10.1 — the geometric definition

A **connection** on $P$ is a smooth, $G$-equivariant splitting

$$T_uP = H_uP \oplus V_uP$$

such that:

(i) every smooth vector field $X$ on $P$ splits smoothly as $X = X^H + X^V$;

(ii) $\boxed{H_{ug}P = R_{g*}H_uP}$ for all $u\in P$, $g \in G$.

Condition (ii) says: once you know $H_uP$ at one point of a fibre, the right action of $G$ generates the horizontal subspace **at every other point of that fibre**. This is exactly what makes "parallel transport commutes with gauge transformations" true later on.

> This definition is deliberately abstract and chart-independent — it is the cleanest way to see that a connection is a piece of *intrinsic geometry* on $P$, with no a priori connection to gauge potentials. The link to physics comes next.

### 1.3 The connection one-form (Ehresmann connection)

To compute, you want an algebraic object that *picks out* $H_uP$ automatically. This is the **connection one-form** $\omega \in \mathfrak{g}\otimes T^*P$:

$$\text{(i) } \omega(A^\#) = A,\ A\in\mathfrak{g}; \qquad \text{(ii) } R_g^*\omega = \mathrm{Ad}_{g^{-1}}\,\omega,\ \text{i.e. } \omega_{ug}(R_{g*}X) = g^{-1}\omega_u(X)g.$$

Define $H_uP \equiv \ker\omega = \{X \in T_uP \mid \omega(X)=0\}$.

**Proposition 10.1.** This $H_uP$ automatically satisfies $R_{g*}H_uP = H_{ug}P$ — i.e. $\omega$'s kernel reproduces Definition 10.1 exactly. So *connection* and *connection one-form* are equivalent notions; $\omega$ is also called the **Ehresmann connection**.

Think of $\omega$ as "the part of a tangent vector that is purely vertical, expressed as a Lie algebra element." It projects $T_uP$ onto $V_uP \cong \mathfrak{g}$.

### 1.4 Local connection form = the gauge potential

Choose a local section $\sigma_i: U_i \to \pi^{-1}(U_i)$. Pull $\omega$ back:

$$\boxed{\mathcal{A}_i \equiv \sigma_i^*\omega \in \mathfrak{g}\otimes\Omega^1(U_i).}$$

**This is the gauge potential.** Theorem 10.1 shows the converse holds too: given any $\mathfrak{g}$-valued one-form $\mathcal{A}_i$ on $U_i$ and a section $\sigma_i$, one can manufacture a connection $\omega$ on $P$ realizing it, via

$$\omega_i \equiv g_i^{-1}\pi^*\mathcal{A}_i\, g_i + g_i^{-1}\,d_P g_i,$$

where $g_i$ is the canonical trivialization $u = \sigma_i(p)g_i$. (This is the same combination — "vector-potential part + pure-gauge part" — that recurs throughout the chapter.)

### 1.5 Compatibility condition = gauge transformation across patches

For $\omega$ to be **globally** well defined, the local pieces $\{\mathcal{A}_i\}$ on overlapping charts must agree once you account for how sections transform. With $\sigma_j(p) = \sigma_i(p) t_{ij}(p)$ (the transition function), Lemma 10.1 gives

$$\sigma_{j*}X = R_{t_{ij}*}(\sigma_{i*}X) + (t_{ij}^{-1}\,dt_{ij}(X))^\#,$$

and applying $\omega$ yields the **compatibility condition**:

$$\boxed{\mathcal{A}_j = t_{ij}^{-1}\mathcal{A}_i\, t_{ij} + t_{ij}^{-1}\,dt_{ij}.}$$

In components: $\mathcal{A}_{j\mu} = t_{ij}^{-1}\mathcal{A}_{i\mu}t_{ij} + t_{ij}^{-1}\partial_\mu t_{ij}$.

> **This is exactly the gauge transformation rule of physics.** $t_{ij}$ are the "large," patch-to-patch gauge transformations; if instead you keep the same patch but switch section by $\sigma_2(p) = \sigma_1(p)g(p)$ (Exercise 10.2), you get the more familiar "small" gauge transformation
> $$\mathcal{A}_2 = g^{-1}\mathcal{A}_1 g + g^{-1}\,dg.$$

**Example 10.1 ($U(1)$).** With $t_{ij}(p) = \exp[i\Lambda(p)]$, this reduces to $\mathcal{A}_j = \mathcal{A}_i + i\,d\Lambda$, i.e. $\mathcal{A}_{j\mu} = \mathcal{A}_{i\mu}+i\partial_\mu\Lambda$. The connection $\mathcal{A}_\mu$ differs from the textbook vector potential $A_\mu$ by a factor of $i$: $\mathcal{A}_\mu = iA_\mu$.

> **Key conceptual point:** $\omega$ itself carries the *global* information about the bundle. An individual $\mathcal{A}_i$ only describes the (always-trivial) piece $\pi^{-1}(U_i)$. It is the *whole family* $\{\mathcal{A}_i\}$, glued by the compatibility condition, that encodes the twisting — e.g. the Dirac monopole needs (at least) two gauge potentials, because no single one is globally smooth.

### 1.6 Horizontal lift and parallel transport

**Definition 10.3.** Given a curve $\gamma:[0,1]\to M$, a **horizontal lift** $\tilde\gamma$ is a curve in $P$ with $\pi\circ\tilde\gamma=\gamma$ whose tangent vector is always horizontal.

**Theorem 10.2.** Through any $u_0 \in \pi^{-1}(\gamma(0))$ there is a *unique* horizontal lift. Concretely, write $\tilde\gamma(t) = \sigma_i(\gamma(t))g_i(t)$; horizontality $\omega(\tilde X)=0$ becomes the linear ODE

$$\boxed{\frac{dg_i(t)}{dt} = -\mathcal{A}_i(X)\,g_i(t)} \qquad\Longrightarrow\qquad g_i(\gamma(t)) = \mathcal{P}\exp\left(-\int_{\gamma(0)}^{\gamma(t)} \mathcal{A}_{i\mu}\,dx^\mu\right),$$

the **path-ordered exponential**, with $\mathcal{P}$ needed because $\mathcal{A}_{i\mu}$ at different points generally don't commute.

The endpoint $u_1 = \tilde\gamma(1)$ is the **parallel transport** of $u_0$ along $\gamma$, giving a map $\Gamma(\tilde\gamma): \pi^{-1}(\gamma(0)) \to \pi^{-1}(\gamma(1))$.

**Corollary 10.1.** $\Gamma(\tilde\gamma)$ **commutes with the right action**: $R_g\Gamma(\tilde\gamma) = \Gamma(\tilde\gamma)R_g$. (This is exactly condition (ii) of Definition 10.1 paying off.) Also $\Gamma(\widetilde{\alpha*\beta}) = \Gamma(\tilde\beta)\circ\Gamma(\tilde\alpha)$ (concatenated paths compose) and $\Gamma(\tilde\gamma^{-1}) = \Gamma(\tilde\gamma)^{-1}$.

**Worked Example 10.2/10.3.** Take $P(M,\mathbb{R}) \cong M\times\mathbb{R}$ over $M=\mathbb{R}^2-\{0\}$, connection $\omega = \frac{y\,dx-x\,dy}{x^2+y^2} + df$. Lifting the unit circle $\gamma(t)=(\cos2\pi t,\sin2\pi t)$ starting at $f=0$ gives the **helix** $\tilde\gamma(t) = ((\cos2\pi t,\sin2\pi t),\,2\pi t)$. Going once around the circle, $f$ shifts by $2\pi$ — the lift **fails to close**. That failure-to-close is the prototype of holonomy.

---

## 2. Holonomy

### 2.1 Definitions

A **loop** $\gamma\in C_p(M)$ (i.e. $\gamma(0)=\gamma(1)=p$) defines a transformation $\tau_\gamma: \pi^{-1}(p)\to\pi^{-1}(p)$ by horizontal-lifting and reading off the endpoint. Since $\Gamma$ commutes with the right action, $\tau_\gamma(ug) = \tau_\gamma(u)g$.

The **holonomy group** at $u$ is

$$\Phi_u \equiv \{g\in G \mid \tau_\gamma(u)=ug,\ \gamma\in C_p(M)\} \le G.$$

It really is a *group*: loop concatenation gives $g_{\alpha*\beta} = g_\beta g_\alpha$ (10.23); the constant loop gives the identity; the reverse loop gives the inverse.

**Conjugation properties (Exercise 10.5):**
$$\Phi_{ua} \cong a^{-1}\Phi_u a, \qquad \Phi_u \cong \Phi_{u'} \text{ if } u,u' \text{ lie on the same horizontal lift},$$
and if $M$ is connected, all $\Phi_u$ ($u$ ranging over all of $P$) are **isomorphic** to each other.

**In local form (Exercise 10.6):** for a loop $\gamma$ confined to one chart $U_i$ with gauge potential $\mathcal{A}_i$,

$$\boxed{g_\gamma = \mathcal{P}\exp\left(-\oint_\gamma \mathcal{A}_{i\mu}\,dx^\mu\right).}$$

This is precisely the **Wilson loop** of gauge theory.

The **restricted holonomy group** $\Phi^0_u$ uses only loops homotopic to a point — it measures *local* (infinitesimal) curvature effects, as opposed to global topology.

---

## 3. Curvature

### 3.1 Covariant derivative on $P$ and the curvature two-form

Given $\phi \in \Omega^r(P)\otimes V$ (a vector-valued $r$-form on $P$), define the **covariant derivative**

$$\mathrm{D}\phi(X_1,\dots,X_{r+1}) \equiv d_P\phi(X_1^H,\dots,X_{r+1}^H)$$

— i.e. project every argument to its horizontal part *before* exterior-differentiating. This single operation, applied to $\omega$ itself, **defines the curvature**:

$$\boxed{\Omega \equiv \mathrm{D}\omega \in \Omega^2(P)\otimes\mathfrak{g}.}$$

**Proposition 10.2.** $R_a^*\Omega = a^{-1}\Omega a$ — curvature transforms tensorially (no inhomogeneous piece, unlike $\omega$ itself). This is the geometric reason $F_{\mu\nu}$ transforms covariantly under gauge transformations while $A_\mu$ does not.

### 3.2 Cartan's structure equation

**Theorem 10.3 (Cartan's structure equation).**

$$\boxed{\Omega(X,Y) = d_P\omega(X,Y) + [\omega(X),\omega(Y)]} \qquad\text{equivalently}\qquad \boxed{\Omega = d_P\omega + \omega\wedge\omega.}$$

*Proof sketch:* check separately on (horizontal, horizontal), (horizontal, vertical), (vertical, vertical) pairs, using $\omega(X^H)=0$ and the Maurer–Cartan-type identity $d_P\omega(X,Y) = X\omega(Y)-Y\omega(X)-\omega([X,Y])$, plus the fact (**Lemma 10.2**) that $[\text{horizontal},\text{vertical}]$ is horizontal.

### 3.3 Geometric meaning: curvature measures non-closure of infinitesimal loops

For horizontal $X,Y$: $\Omega(X,Y) = -\omega([X,Y])$. Take an infinitesimal coordinate parallelogram with sides $\varepsilon\partial/\partial x^1$, $\delta\partial/\partial x^2$; their horizontal lifts $X,Y$ satisfy $\pi_*[X,Y]^H = \epsilon\delta[\partial_1,\partial_2]=0$, i.e. **$[X,Y]$ is purely vertical**. So the horizontal lift of the little loop fails to close, by a vertical displacement; $\Omega(X,Y)$ is exactly *that* displacement, expressed as a Lie algebra element. This is the bundle-theoretic analogue of "Riemann curvature = non-commutativity of parallel transport" from Chapter 7.

**Theorem 10.4 (Ambrose–Singer).** The Lie algebra $\mathfrak{h}$ of the holonomy group $\Phi_{u_0}$ equals the subalgebra of $\mathfrak{g}$ spanned by all values $\Omega_u(X,Y)$, $X,Y\in H_uP$, with $u$ ranging over the horizontal lift through $u_0$. **In words: curvature generates holonomy.** Local curvature (an infinitesimal object) builds up, via integration, into the global holonomy group.

### 3.4 Local form: the Yang–Mills field strength

Pull back: $\mathcal{F}\equiv\sigma^*\Omega$. From Cartan's equation,

$$\boxed{\mathcal{F} = d\mathcal{A} + \mathcal{A}\wedge\mathcal{A}}, \qquad \mathcal{F}_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + [\mathcal{A}_\mu,\mathcal{A}_\nu].$$

Expanding $\mathcal{A}_\mu = A_\mu{}^\alpha T_\alpha$, $\mathcal{F}_{\mu\nu}=F_{\mu\nu}{}^\alpha T_\alpha$ in a basis with $[T_\alpha,T_\beta]=f_{\alpha\beta}{}^\gamma T_\gamma$ recovers the textbook Yang–Mills field strength:

$$\boxed{F_{\mu\nu}{}^\alpha = \partial_\mu A_\nu{}^\alpha - \partial_\nu A_\mu{}^\alpha + f_{\beta\gamma}{}^\alpha A_\mu{}^\beta A_\nu{}^\gamma.}$$

**Theorem 10.5 (compatibility for $\mathcal{F}$).** $\mathcal{F}_j = \mathrm{Ad}_{t_{ij}^{-1}}\mathcal{F}_i = t_{ij}^{-1}\mathcal{F}_i t_{ij}$ — i.e. the field strength transforms **homogeneously** (tensorially) across patches, unlike $\mathcal{A}$.

### 3.5 The Bianchi identity

Globally: $\mathrm{D}\Omega = 0$ (the covariant derivative of the curvature vanishes — this is automatic from the construction, not an extra assumption). Locally,

$$\boxed{\mathcal{D}\mathcal{F} \equiv d\mathcal{F} + [\mathcal{A},\mathcal{F}] = 0.}$$

For $U(1)$ this collapses to the familiar $d\mathcal{F}=0$ (since the bracket vanishes), which is just $dF=0$, i.e. two of Maxwell's four equations.

---

## 4. The Covariant Derivative on Associated Vector Bundles

### 4.1 Why this matters

In physics you don't usually differentiate sections of $P$ itself — you differentiate matter fields, which live in an **associated vector bundle** $E = P\times_\rho V$. A connection on $P$ automatically induces a covariant derivative on every such $E$, completely determined by $\omega$ (modulo the choice of representation $\rho$).

### 4.2 Definition via horizontal lifts

Represent a section as $s(p) = [(\sigma_i(p),\xi(p))]$ (fixing a gauge via the local section $\sigma_i$). A section is **parallel transported** along $\gamma$ if it's constant *along a horizontal lift* of $\gamma$ — not if $\xi(\gamma(t))$ is literally constant (that statement is gauge-dependent and meaningless on its own). This definition is intrinsic: switching horizontal lift by $a\in G$ just multiplies the fibre coordinate by $a^{-1}$, consistently.

**Covariant derivative:**

$$\boxed{\nabla_X s \equiv \Big[\Big(\tilde\gamma(0),\ \frac{d}{dt}\eta(\gamma(t))\Big|_{t=0}\Big)\Big]}$$

— independent of the choice of horizontal lift and of local trivialization (this independence is checked explicitly using the compatibility condition (10.9)). $\nabla$ extends to a map $\Gamma(M,E)\to\Gamma(M,E)\otimes\Omega^1(M)$, **$\mathbb{R}$-linear and satisfying the Leibniz rule** (Exercise 10.8):

$$\nabla_X(fs) = X[f]s + f\nabla_X s,\qquad \nabla(fs) = (df)s + f\nabla s,\qquad \nabla_{fX}s = f\nabla_X s.$$

### 4.3 Local coordinate expression

With basis sections $e_\alpha(p)\equiv[(\sigma_i(p),e_\alpha^0)]$,

$$\boxed{\nabla_{\partial/\partial x^\mu}e_\alpha = \mathcal{A}_{i\mu}{}^\beta{}_\alpha\, e_\beta}, \qquad \boxed{\nabla_X s = \frac{dx^\mu}{dt}\Big\{\frac{\partial\xi^\alpha}{\partial x^\mu} + \mathcal{A}_{i\mu}{}^\alpha{}_\beta\,\xi^\beta\Big\}\,e_\alpha}$$

for a general section $s=\xi^\alpha e_\alpha$. This is *the* practical formula — "ordinary derivative + connection-coefficient correction" — used everywhere in physics. It's manifestly well-defined across patches because $\mathcal{A}_i$ transforms exactly so as to cancel the change of trivialization (using the compatibility condition again).

**Example 10.4 (recovering Chapter 7).** For $E=TM$ associated with the frame bundle $FM = P(M,GL(m,\mathbb{R}))$, writing $\mathcal{A}_i = \Gamma^\alpha{}_{\mu\beta}\,dx^\mu$ recovers $\nabla_{\partial/\partial x^\mu}e_\alpha = \Gamma^\beta{}_{\mu\alpha}e_\beta$ and $\nabla_{\partial/\partial x^\mu}s = (\partial_\mu X_i^\alpha+\Gamma^\alpha{}_{\mu\beta}X^\beta)e_\alpha$ — exactly the affine connection / Christoffel symbols of Riemannian geometry. **A connection on a principal bundle is the common ancestor of both the Christoffel connection and the gauge potential.**

**Examples 10.5/10.6 (QED & $SU(2)$ Yang–Mills).** A charged scalar $\phi$: associated $\mathbb{C}$-bundle of $P(M,U(1))$, giving $\nabla_X\phi = X^\mu(\partial_\mu\Phi+\mathcal{A}_{i\mu}\Phi)e$ — the familiar minimal coupling $\partial_\mu - ieA_\mu$. An $SU(2)$ doublet: associated $\mathbb{C}^2$-bundle of $P(M,SU(2))$, giving $\nabla_X\phi = X^\mu(\partial_\mu\Phi^\alpha + \mathcal{A}_{i\mu}{}^\alpha{}_\beta\Phi^\beta)e_\alpha$.

### 4.4 Curvature rederived as $\nabla\nabla$

Extend $\nabla$ to vector-valued $p$-forms via $\nabla(s\otimes\eta)\equiv(\nabla s)\wedge\eta+s\otimes d\eta$. Then

$$\boxed{\nabla\nabla e_\alpha = e_\beta\otimes\mathcal{F}_i{}^\beta{}_\alpha}$$

— i.e. **curvature is precisely the failure of $\nabla$ to square to zero**, the bundle-theoretic generalization of "$d^2=0$ but $\nabla^2 \ne 0$ measures curvature" familiar from Riemannian geometry.

### 4.5 Metric and Hermitian connections

A connection $\nabla$ is **metric** if it preserves a fibre inner product $g$: $d[g(s,s')] = g(\nabla s,s')+g(s,\nabla s')$. **Theorem 10.6:** the covariant derivative built from an **orthonormal frame** is automatically metric. With structure group $O(k)$, the connection one-form is **skew**: $\omega^\alpha{}_\beta = -\omega^\beta{}_\alpha$. (If $E=TM$ and torsion-freeness is additionally imposed, this *is* the Levi-Civita connection.)

For complex/holomorphic bundles, the analogous structure is a **Hermitian connection** compatible with a Hermitian metric $h$ (unique once $h$ is fixed), splitting as $\nabla = D+\bar D$ with $\bar D=\bar\partial$. Its curvature $\mathcal{F}=d\mathcal{A}+\mathcal{A}\wedge\mathcal{A}$ is automatically **skew-Hermitian** ($\mathcal{A}^\alpha{}_\beta = -\bar{\mathcal{A}}^\beta{}_\alpha$) and turns out to be a **$(1,1)$-form** — a fact that becomes central to Chern class theory and Kähler geometry later in the book.

---

## 5. Gauge Theories — the Dictionary in Action

### 5.1 $U(1)$ gauge theory = Maxwell

Over (contractible) Minkowski space $\mathbb{R}^4$, the bundle is automatically trivial (Corollary 9.1), so a single global $\mathcal{A}=\mathcal{A}_\mu dx^\mu$ suffices. $\mathcal{F}=d\mathcal{A}$ is automatically exact $\Rightarrow$ Bianchi identity $d\mathcal{F}=0$ holds for free, reproducing two of Maxwell's equations:
$$\nabla\cdot\mathbf{B}=0,\qquad \nabla\times\mathbf{E}+\partial_t\mathbf{B}=0.$$
The dynamical content (the *other* two Maxwell equations) comes from extremizing the **Maxwell action** $\mathcal{S}_M[\mathcal{A}] = \frac14\int \mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu}d^4x = -\frac14\int F_{\mu\nu}F^{\mu\nu}d^4x$, giving the equation of motion $\partial_\mu\mathcal{F}^{\mu\nu}=0$, i.e. $\nabla\cdot\mathbf{E}=0$, $\nabla\times\mathbf{B}-\partial_t\mathbf{E}=0$.

### 5.2 The Dirac magnetic monopole

Now the base is $\mathbb{R}^3-\{0\} \simeq S^2$ (nontrivial!), so a single $\mathcal{A}$ does *not* exist globally. Use the Wu–Yang potentials $\mathcal{A}_N = ig(1-\cos\theta)d\phi$, $\mathcal{A}_S = -ig(1+\cos\theta)d\phi$. The transition function $t_{NS}(\phi)=\exp[i\varphi(\phi)]$ satisfies $d\varphi = 2g\,d\phi$, so going once around the equator,

$$\Delta\varphi = \int_0^{2\pi}2g\,d\phi = 4\pi g.$$

Single-valuedness of $t_{NS}$ forces

$$\boxed{\Delta\varphi/2\pi = 2g \in \mathbb{Z}}$$

— **Dirac's quantization condition.** The same integer is the total monopole flux $\Phi = \int_{S^2}\mathbf{B}\cdot d\mathbf{S} = \int_{U_N}dA_N+\int_{U_S}dA_S = 4\pi g$. **The curvature (pair of local field strengths) is what carries the bundle's topological twist** — this is the bridge to Chern classes in Chapter 11.

### 5.3 The Aharonov–Bohm effect

A solenoid with flux $\Phi$ at the origin of $M=\mathbb{R}^2-\{0\}$; outside, $\mathbf{B}=0$ but $\mathbf{A}\ne 0$:
$$\mathbf{A}(\mathbf{r}) = \Big(-\frac{y\Phi}{2\pi r^2},\ \frac{x\Phi}{2\pi r^2},\ 0\Big).$$
Even though $F=dA=0$ (the connection is **locally flat**), the relevant bundle is **not trivial**, and the phase difference between two paths (one on each side of the solenoid) is
$$e\oint_\gamma A\cdot d\mathbf{r}' = e\Phi$$
by Stokes' theorem. Two flux values give the same interference pattern iff $e(\Phi_a-\Phi_b)=2\pi n$. **Equivalently:** parallel-transporting a wavefunction once around $S^1$ enclosing the solenoid, with local connection $\mathcal{A}=i\frac{\Phi}{2\pi}d\theta$, gives the holonomy $\psi(0)\mapsto e^{-i\Phi}\psi(0)$.

> **Lesson:** even a *flat* connection ($\mathcal{F}=0$ everywhere) can have **nontrivial holonomy** if the base is not simply connected. Curvature governs *local* parallel transport; holonomy on noncontractible loops is a genuinely separate, more global, invariant — this is precisely the gap closed by the (unrestricted) holonomy group of §2 versus the restricted one.

### 5.4 $SU(2)$ Yang–Mills and instantons

Over (contractible) $\mathbb{R}^4$ a single gauge potential $\mathcal{A}=A_\mu{}^\alpha T_\alpha\,dx^\mu$ suffices, $T_\alpha=\sigma_\alpha/2i$. Field strength and Bianchi identity are the non-Abelian analogues of §3.4–3.5. The **Euclidean** Yang–Mills action is

$$\mathcal{S}^E_{YM}[\mathcal{A}] = \tfrac14\int_M \mathrm{tr}(\mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu}) = -\tfrac12\int_M\mathrm{tr}(\mathcal{F}\wedge{*}\mathcal{F}),$$

minimized by **(anti-)self-dual** configurations $\mathcal{F}_{\mu\nu}=\pm{*}\mathcal{F}_{\mu\nu}$ — the **instantons**.

**Topological classification.** Finite action requires $\mathcal{A}_\mu(x)\to g(x)^{-1}\partial_\mu g(x)$ as $|x|\to\infty$; this defines a map $g: S^3_\infty \to SU(2)$, classified by $\pi_3(SU(2))=\mathbb{Z}$. Compactifying $\mathbb{R}^4$ to $S^4$ (North Pole = origin, South Pole = $\infty$), and choosing the gauge $\mathcal{A}_S\equiv 0$, one finds $g(x)$ is *exactly* the transition function $t_{NS}$ between the two hemispheres — so classifying boundary conditions = classifying bundle twists, exactly as in §I.5.5.

Explicit homotopy classes: the constant map $g_0\equiv e$ (class 0); the identity map $g_1: x\mapsto r^{-1}(x^4I_2+x^i\sigma_i)$ (class 1); and $g_n=(g_1)^n$ (class $n$).

**The topological charge formula.** Define $K \equiv \mathrm{tr}[\mathcal{A}\,d\mathcal{A}+\frac23\mathcal{A}^3]$ (the **Chern–Simons form**); then $\mathrm{tr}\,\mathcal{F}^2 = dK$ (Lemma 10.3), and Stokes' theorem gives

$$\boxed{n = \frac{1}{24\pi^2}\int_{S^3}\mathrm{tr}(g^{-1}dg)^3 = \frac12\int_{S^4}\mathrm{tr}\Big(\frac{i\mathcal{F}}{2\pi}\Big)^2 = -\frac{1}{8\pi^2}\int_{S^4}\mathrm{tr}\,\mathcal{F}^2}$$

(Theorem 10.7). This integer **instanton number** is exactly analogous to the **monopole flux integer** $2g$ of §5.2 — both are curvature integrals that compute the homotopy class of a transition function. ($\mathrm{tr}\,\mathcal{F}^2$ will later be identified with the **second Chern character**, and $K$ with its **Chern–Simons form** — Chapter 11.)

---

## 6. Berry's Phase

### 6.1 Setup

A Hamiltonian $H(\mathbf{R})$ depends adiabatically on parameters $\mathbf{R}(t)$. Starting in the $n$th eigenstate, naive WKB-type guesses fail to solve Schrödinger's equation; the correct ansatz needs an *extra phase* $\eta_n(t)$:

$$|\psi(t)\rangle = \exp\Big[i\eta_n(t) - i\int_0^t E_n(\mathbf{R}(s))\,ds\Big]\,|n,\mathbf{R}(t)\rangle, \qquad \frac{d\eta_n}{dt} = i\langle n,\mathbf{R}(t)|\tfrac{d}{dt}|n,\mathbf{R}(t)\rangle.$$

For a **closed loop** $\mathbf{R}(0)=\mathbf{R}(T)$,

$$\boxed{\eta_n(T) = i\oint \langle n,\mathbf{R}|\nabla_{\mathbf{R}}|n,\mathbf{R}\rangle\cdot d\mathbf{R}}$$

— **Berry's phase** (Berry 1984). It need not vanish even though $\mathbf{R}$ returns to its start, because the integrand is generally not an exact differential.

### 6.2 The bundle-theoretic picture (Simon's insight)

A quantum state is only physical up to phase: $[|\mathbf{R}\rangle]\equiv\{g|\mathbf{R}\rangle\mid g\in U(1)\}$. This makes the parameter space $M$ the base of a **$U(1)$ principal bundle** $P(M,U(1))$, with fibre = phase choices. Fixing a phase convention at each $\mathbf{R}$ is a **local section**; **Berry's connection** is

$$\boxed{\mathcal{A} = \langle\mathbf{R}|d|\mathbf{R}\rangle}, \qquad \boxed{\mathcal{F} = d\mathcal{A} = (d\langle\mathbf{R}|)\wedge(d|\mathbf{R}\rangle)} \ \ (\textbf{Berry's curvature}).$$

One checks $\mathcal{A}$ is anti-Hermitian (from $d\langle\mathbf{R}|\mathbf{R}\rangle=0$) and that the compatibility condition (10.9) holds across charts — confirming this *is* a genuine Ehresmann connection. **Berry's phase is then literally the holonomy of this connection:**

$$\boxed{\eta(1) = i\oint_{\mathbf{R}} \mathcal{A} = i\int_S \mathcal{F}}$$

(Exercise 10.14), where $S$ is any surface bounded by the loop. This single line is the payoff of the entire chapter: a famous, experimentally measured quantum-mechanical phase is *exactly* the same geometric object as the Wilson loop / Aharonov–Bohm phase / Wu–Yang transition data seen earlier.

### 6.3 Worked Example: spin-$\tfrac12$ in a magnetic field

$H(\mathbf{R}) = \mathbf{R}\cdot\boldsymbol{\sigma}$, eigenvalue $+|\mathbf{R}|$. In polar coordinates $(\theta,\phi)$ on the parameter sphere $S^2$ (with the field magnitude fixed), two local eigenstate choices ("N" near $\theta=0$ pole, "S" near $\theta=\pi$ pole) give

$$\mathcal{A}_N = \tfrac{i}{2}(1-\cos\theta)\,d\phi,\qquad \mathcal{A}_S = -\tfrac{i}{2}(1+\cos\theta)\,d\phi,$$

related by the transition function $g=e^{-i\phi}$ — **this is exactly the Wu–Yang monopole of strength $-\tfrac12$.** Total flux $\Phi = -2\pi$. The degeneracy point $\mathbf{R}=0$ (where the two-level system's eigenvalues coincide) plays the role of the **monopole location**: a level crossing is a curvature singularity.

> **Big-picture takeaway for Berry's phase:** wherever a family of quantum states is parametrized smoothly except at isolated degeneracies, you automatically get a nontrivial $U(1)$ bundle over the parameter space, and adiabatic transport around a loop picks up a holonomy phase — mathematically indistinguishable from a magnetic monopole sitting at the degeneracy.

---

## 7. Putting It All Together: One Table

| Concept (geometry) | Concept (gauge theory) | Concept (Berry/QM) |
|---|---|---|
| Principal bundle $P(M,G)$ | spacetime + gauge group | parameter space + state phase |
| Connection one-form $\omega$ | — | — |
| Local connection form $\mathcal{A}_i=\sigma_i^*\omega$ | gauge potential $A_\mu$ | Berry connection $\langle\mathbf{R}|d|\mathbf{R}\rangle$ |
| Curvature $\Omega=D\omega$ | — | — |
| Local curvature $\mathcal{F}=d\mathcal{A}+\mathcal{A}\wedge\mathcal{A}$ | field strength $F_{\mu\nu}$ | Berry curvature |
| Horizontal lift | parallel transport of charge/color | adiabatic transport |
| Holonomy of a loop | Wilson loop | Berry's phase |
| Transition function $t_{ij}$ | gauge transformation between patches | phase convention change |
| $\pi_1(U(1))=\mathbb{Z}$ twisting | Dirac monopole charge | "Berry monopole" at level crossing |
| $\pi_3(SU(2))=\mathbb{Z}$ twisting | instanton number | — |

---

## 8. Glossary (Chapter 10 quick reference)

- **Vertical subspace $V_uP$** — tangent to the fibre; $\pi_*$-image is zero.
- **Fundamental vector field $A^\#$** — generator of the right $\exp(tA)$-action; isomorphism $\mathfrak{g}\cong V_uP$.
- **Horizontal subspace $H_uP$** — connection-dependent complement of $V_uP$; $R_g$-equivariant.
- **Connection one-form $\omega$** — $\mathfrak{g}$-valued 1-form on $P$; projects onto $V_uP\cong\mathfrak{g}$; reproduces $A$ on fundamental fields; transforms by $\mathrm{Ad}_{g^{-1}}$ under right action.
- **Local connection form / gauge potential $\mathcal{A}_i=\sigma_i^*\omega$** — physicists' $A_\mu$ (up to factor $i$); patch-dependent.
- **Compatibility condition** — $\mathcal{A}_j = t_{ij}^{-1}\mathcal{A}_it_{ij}+t_{ij}^{-1}dt_{ij}$; the gauge transformation law.
- **Horizontal lift / parallel transport** — unique curve in $P$ projecting to a given base curve with horizontal tangent everywhere; governed by a linear ODE solved by a path-ordered exponential.
- **Holonomy group $\Phi_u$** — subgroup of $G$ generated by parallel transport around all loops at $\pi(u)$; restricted version $\Phi_u^0$ uses only contractible loops.
- **Covariant derivative $D$ on $P$** — exterior derivative with horizontal projection of arguments.
- **Curvature $\Omega=D\omega$** — transforms tensorially ($\mathrm{Ad}_{a^{-1}}$, no inhomogeneous term); Cartan's equation $\Omega=d_P\omega+\omega\wedge\omega$.
- **Yang–Mills field strength $\mathcal{F}=\sigma^*\Omega = d\mathcal{A}+\mathcal{A}\wedge\mathcal{A}$** — local form of curvature.
- **Bianchi identity** — $D\Omega=0$, locally $d\mathcal{F}+[\mathcal{A},\mathcal{F}]=0$.
- **Ambrose–Singer theorem** — curvature values span the Lie algebra of the holonomy group.
- **Covariant derivative $\nabla$ on an associated bundle $E$** — induced from $\omega$; "ordinary derivative + $\mathcal{A}$-correction"; $\nabla\nabla e_\alpha = e_\beta\otimes\mathcal{F}^\beta{}_\alpha$.
- **Metric / Hermitian connection** — preserves a (real / Hermitian) fibre inner product; unique once the metric and the requirement $\bar D=\bar\partial$ (Hermitian case) are fixed.
- **Wilson loop** — holonomy expressed as a path-ordered exponential of $\mathcal{A}$ around a loop.
- **Instanton number / Chern–Simons form $K$** — topological charge $n=\frac{1}{24\pi^2}\int_{S^3}\mathrm{tr}(g^{-1}dg)^3 = -\frac{1}{8\pi^2}\int_{S^4}\mathrm{tr}\,\mathcal{F}^2$.
- **Berry's connection / curvature / phase** — Ehresmann connection on the $U(1)$ bundle of quantum phases over parameter space; the phase picked up around an adiabatic loop is exactly its holonomy.


---

## 9. How This Connects Forward

Chapter 10 ends with curvature integrals ($\mathrm{tr}\,\mathcal{F}^2$, $\oint\mathcal{A}$) that are manifestly gauge-invariant and topological. Chapter 11 (**characteristic classes**) makes this systematic: $\mathrm{tr}\,\mathcal{F}^2$ becomes the **second Chern character**, $K$ its **Chern–Simons form**, and the integers we kept computing by hand (monopole charge, instanton number) become specific evaluations of universal polynomials in the curvature — the **Chern classes** and **Pontryagin classes** — that depend only on the topological type of the bundle, not on the particular connection chosen.

---
---

# PART III — Characteristic Classes (Chapter 11)

## 0. The Big Picture 

Chapters 9–10 built fibre bundles and connections, and kept stumbling onto curvature integrals that always came out to be integers, independent of which gauge potential was chosen: the monopole charge $n = \frac{i}{2\pi}\oint_{S^2}\mathcal F$, the instanton number $n=-\frac{1}{8\pi^2}\int_{S^4}\mathrm{tr}\,\mathcal F^2$. Chapter 11 explains *why this always happens* and turns it into a systematic machine.

> **Slogan:** Pick an invariant polynomial $P$ on the Lie algebra $\mathfrak g$ of the structure group. Plug in the curvature: $P(\mathcal F)$ is automatically **closed**, $dP(\mathcal F)=0$, and its cohomology class $\chi_E(P)\in H^*(M)$ does **not depend on which connection produced $\mathcal F$**. This is the **characteristic class** of the bundle $E$ associated to $P$ — and it vanishes identically whenever $E$ is trivial.

Different choices of $P$ give different named families of classes:

| Choice of invariant polynomial | Resulting class |
|---|---|
| $\det(I+i\mathcal F/2\pi)$ | Chern class $c(\mathcal F)$ |
| $\mathrm{tr}\exp(i\mathcal F/2\pi)$ | Chern character $\mathrm{ch}(\mathcal F)$ |
| $\prod_j x_j/(1-e^{-x_j})$ | Todd class $\mathrm{Td}(\mathcal F)$ |
| $\det(I+\mathcal F/2\pi)$ | Pontryagin class $p(\mathcal F)$ |
| $\mathrm{Pf}(\mathcal F/2\pi)$ | Euler class $e(\mathcal F)$ |
| $\prod_j x_j/\tanh x_j$ | Hirzebruch $L$-polynomial |
| $\prod_j (x_j/2)/\sinh(x_j/2)$ | $\hat A$-genus (Dirac genus) |

There is exactly **one** class in this chapter that breaks the pattern — the **Stiefel–Whitney class** $w_r\in H^r(M;\mathbb Z_2)$ — because it is a genuinely discrete, mod-2 invariant that no curvature-based formula can ever produce. It governs orientability ($w_1$) and the existence of spin structures ($w_2$), which is why it matters so much in physics: fermions need a spin structure to exist at all.

---

## 1. Invariant Polynomials and the Chern–Weil Homomorphism

### 1.1 Symmetric invariant multilinear functions

Let $\mathfrak g$ be the Lie algebra of a matrix group $G$ (typically $GL(k,\mathbb C)$, $U(k)$, or $SU(k)$). A symmetric $\mathbb C$-valued $r$-linear map

$$\tilde P:\underbrace{\mathfrak g\times\cdots\times\mathfrak g}_{r}\to\mathbb C$$

is **invariant** if, for every $g\in G$ and $A_i\in\mathfrak g$,

$$\tilde P(\mathrm{Ad}_gA_1,\dots,\mathrm{Ad}_gA_r)=\tilde P(A_1,\dots,A_r),\qquad \mathrm{Ad}_gA\equiv g^{-1}Ag.$$

Write $I^r(G)$ for the invariant $r$-linear forms; $I^*(G)=\bigoplus_r I^r(G)$ is an algebra. The basic example is the **symmetrized trace**

$$\mathrm{str}(A_1,\dots,A_r)=\frac{1}{r!}\sum_P \mathrm{tr}(A_{P(1)}\cdots A_{P(r)}).$$

### 1.2 Invariant polynomials and polarization

Plugging the same element into every slot, $P(A)\equiv\tilde P(A,\dots,A)$, gives a degree-$r$ **invariant polynomial**: $P(g^{-1}Ag)=P(A)$. Every invariant polynomial is a sum of products of the basic traces $P_r(A)=\mathrm{tr}(A^r)$.

Conversely, $P$ determines $\tilde P$ (its **polarization**) by expanding $P(t_1A_1+\cdots+t_rA_r)$ and reading off $1/r!$ times the coefficient of $t_1t_2\cdots t_r$. Worked example: for $P(A)=\mathrm{tr}(A^3)$,

$$\tilde P(A_1,A_2,A_3)=\tfrac12\mathrm{tr}(A_1A_2A_3+A_2A_1A_3)=\mathrm{str}(A_1,A_2,A_3).$$

### 1.3 Extending to Lie-algebra–valued forms

For $\mathfrak g$-valued forms $A_i\eta_i$,

$$\tilde P(A_1\eta_1,\dots,A_r\eta_r)=\eta_1\wedge\cdots\wedge\eta_r\cdot\tilde P(A_1,\dots,A_r),$$

and diagonally $P(A\eta)=\underbrace{\eta\wedge\cdots\wedge\eta}_{r}\cdot P(A)$. This is exactly what lets us plug in the curvature 2-form $\mathcal F$ to get $P(\mathcal F)$.

### 1.4 The Chern–Weil theorem

> **Theorem 11.1 (Chern–Weil).** Let $P$ be an invariant polynomial. Then:
> (a) $dP(\mathcal F)=0$ — $P(\mathcal F)$ is **closed**.
> (b) If $\mathcal F,\mathcal F'$ are curvatures of two *different* connections $\mathcal A,\mathcal A'$ on the same bundle, then $P(\mathcal F')-P(\mathcal F)$ is **exact**.

*Why (a) holds.* Differentiating the invariance identity at $g_t=\exp(tX)$, $t=0$, gives the algebraic identity $\sum_i\tilde P(A_1,\dots,[A_i,X],\dots,A_r)=0$. Feeding in $\mathcal A$ and $\mathcal F$ and using the **Bianchi identity** $\mathcal D\mathcal F=d\mathcal F+[\mathcal A,\mathcal F]=0$, every term cancels, leaving $dP(\mathcal F)=0$.

*Why (b) holds.* Build an interpolating connection $\mathcal A_t=\mathcal A+t\theta$, $\theta=\mathcal A'-\mathcal A$, $t\in[0,1]$, curvature $\mathcal F_t=\mathcal F+t\mathcal D\theta+t^2\theta^2$. One shows $\frac{d}{dt}P_r(\mathcal F_t)=r\,d[\tilde P_r(\theta,\mathcal F_t,\dots,\mathcal F_t)]$, so integrating over $t$:

$$\boxed{P_r(\mathcal F')-P_r(\mathcal F)=d\Big[r\int_0^1\tilde P_r(\mathcal A'-\mathcal A,\mathcal F_t,\dots,\mathcal F_t)\,dt\Big]\equiv d\,TP_r(\mathcal A',\mathcal A).}$$

The bracketed $(2r-1)$-form $TP_r(\mathcal A',\mathcal A)$ is the **transgression** — it reappears in §7 as the Chern–Simons form.

### 1.5 Characteristic classes and the Weil homomorphism

Since $P(\mathcal F)$ is closed and (by part (b)) connection-independent up to exact terms, it defines a well-defined element $\chi_E(P)\in H^*(M)$, the **characteristic class** of $E$ associated to $P$.

> **Theorem 11.2.**
> (a) $\chi_E: I^*(G)\to H^*(M)$, $P\mapsto\chi_E(P)$, is a ring homomorphism (the **Weil homomorphism**): $\chi_E(P_rP_s)=\chi_E(P_r)\wedge\chi_E(P_s)$.
> (b) **Naturality**: for $f:N\to M$, $\chi_{f^*E}=f^*\chi_E$.

> **Corollary 11.1.** Characteristic classes of a **trivial bundle vanish.** (A trivial bundle is the pullback of a bundle over a point, and $H^*(\text{point})$ is trivial in positive degree; naturality then forces $\chi$ to vanish too.)

This corollary is the whole engine of the chapter: a *non-vanishing* characteristic class **proves** non-triviality.

---

## 2. Chern Classes

### 2.1 Definition

For a complex vector bundle $E\to M$, fibre $\mathbb C^k$, structure group $G\subset GL(k,\mathbb C)$, curvature $\mathcal F$ valued in $\mathfrak g$, define the **total Chern class**

$$\boxed{c(\mathcal F)\equiv\det\Big(I+\frac{i\mathcal F}{2\pi}\Big)=1+c_1(\mathcal F)+c_2(\mathcal F)+\cdots}$$

$c_j(\mathcal F)\in\Omega^{2j}(M)$ is the **$j$th Chern class**; it vanishes whenever $2j>\dim M$ or $j>k$.

### 2.2 Computing via diagonalization

Diagonalize $i\mathcal F/2\pi=g^{-1}(i\mathcal F/2\pi)g=\mathrm{diag}(x_1,\dots,x_k)$ (possible with $g\in SU(k)$ when $G=SU(k)$, since $i\mathcal F/2\pi$ is then Hermitian). Then

$$\det(I+A)=\prod_j(1+x_j)=1+\mathrm{tr}\,A+\tfrac12[(\mathrm{tr}\,A)^2-\mathrm{tr}\,A^2]+\cdots+\det A,$$

each term an **elementary symmetric function** of the eigenvalues. Explicitly:

$$c_0=1,\quad c_1(\mathcal F)=\frac{i}{2\pi}\mathrm{tr}\,\mathcal F,\quad c_2(\mathcal F)=\tfrac12\Big(\frac{i}{2\pi}\Big)^2\big[\mathrm{tr}\,\mathcal F\wedge\mathrm{tr}\,\mathcal F-\mathrm{tr}(\mathcal F\wedge\mathcal F)\big],\ \dots,\ c_k(\mathcal F)=\Big(\frac{i}{2\pi}\Big)^k\det\mathcal F.$$

**Worked example ($SU(2)$ bundle, $\dim M=4$).** With $\mathcal F=\mathcal F^\alpha(\sigma_\alpha/2i)$, the Pauli matrices are traceless, so $c_0=1$, $c_1=0$, and

$$c_2(\mathcal F)=\Big(\frac{i}{2\pi}\Big)^2\sum_\alpha\frac{\mathcal F^\alpha\wedge\mathcal F^\alpha}{4}=\det\Big(\frac{i\mathcal F}{2\pi}\Big);$$

higher Chern classes vanish ($k=2$). Integrated over $S^4$, this $c_2$ **is the instanton number** of §II.5.4.

### 2.3 Properties

> **Theorem 11.3.**
> (a) **Naturality:** $c(f^*E)=f^*c(E)$.
> (b) **Whitney sum formula:** $\boxed{c(E\oplus F)=c(E)\wedge c(F)}$ — because the curvature of a Whitney sum is block-diagonal (recall §I.4.6), and $\det$ of a block-diagonal matrix factorizes.

Consequences: $c(\text{trivial bundle})=1$; if $E=E_1\oplus E_2$ with $E_2$ trivial of rank $k_2$, then $c_i(E)=0$ for $k_1<i\le k_1+k_2$.

### 2.4 The splitting principle

If $E$ really were a Whitney sum of $n$ complex **line bundles**, $E=L_1\oplus\cdots\oplus L_n$, the sum formula gives $c(E)=\prod_i(1+x_i)$, $x_i\equiv c_1(L_i)$ — identical in shape to the diagonalized formula of §2.2. The **splitting principle** says we may always *pretend* this is true purely for computing characteristic classes, even when $E$ is not literally such a sum (made rigorous via flag bundles; diagonalizable matrices are dense in $M(k,\mathbb C)$, so any curvature can be approximated by, and behaves algebraically like, a direct sum of line-bundle pieces — the "Chern roots" $x_i$).

### 2.5 Axiomatic characterization

The Chern class is the *unique* assignment satisfying:
1. naturality: $c(f^*E)=f^*c(E)$;
2. $c(E)=\bigoplus_ic_i(E)$, $c_i\in H^{2i}(M)$, $c_i=0$ for $i>\mathrm{rank}(E)$;
3. Whitney sum: $c(E\oplus F)=c(E)c(F)$;
4. normalization: $c(L)=1+x$ for the canonical line bundle $L$ over $\mathbb{C}P^n$.

### 2.6 Universal bundles and classifying spaces

Any rank-$k$ bundle $E\to M$ embeds into a trivial bundle, $E\oplus\bar E\cong M\times\mathbb C^n$ for large $n$, giving a **Gauss map** $f:M\to G_{k,n}(\mathbb C)$ (complex Grassmannian of $k$-planes in $\mathbb C^n$) with $E\cong f^*L_{k,n}(\mathbb C)$. As $n\to\infty$ this stabilizes to the **classifying space** $G_k(\mathbb C)=\bigcup_nG_{k,n}(\mathbb C)$ and **universal bundle** $L_k$.

> **Theorem 11.4.** Every rank-$k$ bundle is $f^*L_k$ for some $f:M\to G_k(\mathbb C)$, and $f^*L_k\cong g^*L_k$ iff $f\simeq g$.

So **classifying complex vector bundles over $M$ reduces to classifying homotopy classes of maps $M\to G_k(\mathbb C)$** — the exact same logic that classified monopoles/instantons by $\pi_1(U(1))$/$\pi_3(SU(2))$ in §I.5, just upgraded from "two-patch transition function" language to "map into a universal space" language.

---

## 3. Chern Characters

### 3.1 Definition

$$\boxed{\mathrm{ch}(\mathcal F)\equiv\mathrm{tr}\exp\Big(\frac{i\mathcal F}{2\pi}\Big)=\sum_{j\ge0}\frac{1}{j!}\mathrm{tr}\Big(\frac{i\mathcal F}{2\pi}\Big)^j.}$$

$\mathrm{ch}_j(\mathcal F)=\frac{1}{j!}\mathrm{tr}(i\mathcal F/2\pi)^j$ is the **$j$th Chern character**; vanishes for $2j>\dim M$.

### 3.2 Relation to Chern classes

Diagonalizing as before, $\mathrm{tr}\exp(A)=\sum_j\exp(x_j)$; expanding in elementary symmetric functions and matching to the Chern classes:

$$\mathrm{ch}_0=k\ (\text{fibre dimension}),\quad \mathrm{ch}_1=c_1,\quad \mathrm{ch}_2=\tfrac12(c_1^2-2c_2),\ \dots$$

### 3.3 Why Chern characters matter

> **Theorem 11.5.**
> (a) Naturality: $\mathrm{ch}(f^*E)=f^*\mathrm{ch}(E)$.
> (b) $\boxed{\mathrm{ch}(E\otimes F)=\mathrm{ch}(E)\wedge\mathrm{ch}(F)}$ **and** $\boxed{\mathrm{ch}(E\oplus F)=\mathrm{ch}(E)\oplus\mathrm{ch}(F)}$.

This is the decisive advantage over the ordinary Chern class: the Chern character turns **both** $\oplus$ and $\otimes$ into simple algebra (sum and product), which is exactly why it is the natural object in the **Atiyah–Singer index theorem**.

### 3.4 Worked examples

- **Magnetic monopole** ($U(1)$ bundle over $S^2$, recall §I.5.4/II.5.2): $\mathrm{ch}(\mathcal F)=1+i\mathcal F/2\pi$ (higher terms vanish on a 2-manifold). The monopole charge $n=\frac{i}{2\pi}\int_{S^2}\mathcal F=\int_{S^2}\mathrm{ch}_1(\mathcal F)\in\mathbb Z$ — **the monopole charge *is* the first Chern number.**
- **$U(1)$ anomaly**: for a $U(1)$ bundle over a $2m$-dimensional manifold, the top Chern character $\mathrm{ch}_m$ is proportional to $\epsilon^{\mu_1\nu_1\cdots\mu_m\nu_m}\mathcal F_{\mu_1\nu_1}\cdots\mathcal F_{\mu_m\nu_m}\,dx^1\wedge\cdots\wedge dx^{2m}$ — exactly the anomaly density in that dimension.
- **Canonical line bundle over $\mathbb{C}P^1\cong S^2$:** Fubini–Study curvature $\mathcal F=-dz\wedge d\bar z/(1+|z|^2)^2$ gives $\mathrm{ch}_1(\mathcal F)=-\frac{1}{\pi}\frac{r\,dr\wedge d\theta}{(1+r^2)^2}$ and $\int_{S^2}\mathrm{ch}_1=-1\in\mathbb Z$.
- **$SU(2)$ instanton over $S^4$** (recall §I.5.5/II.5.4): $\mathrm{ch}(\mathcal F)=2+\mathrm{tr}(i\mathcal F/2\pi)+\tfrac12\mathrm{tr}(i\mathcal F/2\pi)^2$, terminating at $\mathrm{ch}_2$ since $\mathrm{tr}\,\mathcal F=0$ and $\mathcal F^3=0$ for $SU(2)$. The instanton number is exactly $\int_{S^4}\mathrm{ch}_2(\mathcal F)$ — matching the formula boxed in §II.5.4.

---

## 4. Todd Classes

$$\mathrm{Td}(\mathcal F)\equiv\prod_j\frac{x_j}{1-e^{-x_j}}\qquad(\text{splitting principle understood}),$$

expanded with **Bernoulli numbers** $B_k$ ($B_1=\tfrac16,B_2=\tfrac1{30},B_3=\tfrac1{42},B_4=\tfrac1{30},B_5=\tfrac{5}{66},\dots$):

$$\mathrm{Td}(\mathcal F)=1+\tfrac12c_1+\tfrac1{12}(c_1^2+c_2)+\cdots$$

First few terms: $\mathrm{Td}_0=1$, $\mathrm{Td}_1=\tfrac12c_1$, $\mathrm{Td}_2=\tfrac1{12}(c_1^2+c_2)$, $\mathrm{Td}_3=\tfrac1{24}c_1c_2$, $\mathrm{Td}_4=\tfrac1{720}(-c_1^4+4c_1^2c_2+3c_2^2+c_1c_3-c_4)$.

Property: $\mathrm{Td}(E\oplus F)=\mathrm{Td}(E)\wedge\mathrm{Td}(F)$. The Todd class is the key extra ingredient in the **Hirzebruch–Riemann–Roch theorem** and the Dolbeault-complex case of Atiyah–Singer.

---

## 5. Pontryagin and Euler Classes (real vector bundles)

### 5.1 Setup: skew-symmetric curvature

For a real bundle $E$ with a fibre metric, the structure group reduces to $O(k)$; the generators of $\mathfrak o(k)$ are skew-symmetric, so curvature $\mathcal R$ satisfies $\mathcal R^t=-\mathcal R$. Such a matrix block-diagonalizes into $2\times2$ rotation blocks, and a further complex change of basis gives eigenvalue pairs $\pm i\lambda$ (one eigenvalue is forced to $0$ if $k$ is odd).

### 5.2 Total Pontryagin class

$$\boxed{p(\mathcal R)\equiv\det\Big(I+\frac{\mathcal R}{2\pi}\Big).}$$

Since $\mathcal R^t=-\mathcal R$, $\det(I+\mathcal R/2\pi)=\det(I-\mathcal R/2\pi)$, so $p(\mathcal R)$ is **even** in $\mathcal R$: $p(\mathcal R)=1+p_1(\mathcal R)+p_2(\mathcal R)+\cdots$, $p_j\in H^{4j}(M;\mathbb R)$. Diagonalizing $\mathcal R/2\pi\to\mathrm{diag}(-ix_1,ix_1,-ix_2,ix_2,\dots)$, the generating function is $p(\mathcal R)=\prod_{i=1}^{[k/2]}(1+x_i^2)$, giving

$$p_1=-\frac{1}{8\pi^2}\mathrm{tr}\,\mathcal R^2,\qquad p_2=\frac{1}{128\pi^4}\big[(\mathrm{tr}\,\mathcal R^2)^2-2\,\mathrm{tr}\,\mathcal R^4\big],\qquad p_{[k/2]}=\Big(\frac1{2\pi}\Big)^k\det\mathcal R\ \ (\text{the top one}).$$

Property: $p(E\oplus F)=p(E)\wedge p(F)$.

### 5.3 Relation to Chern classes

Complexifying the fibre ($E^{\mathbb C}$), comparing $\det(I+iA)$ to $\det(I+A)$ expansions gives

$$\boxed{p_j(E)=(-1)^jc_{2j}(E^{\mathbb C}).}$$

**Worked example (4-dim Riemannian $M$, curvature 2-form $\mathcal R$ on $TM$, structure group $O(4)$):**

$$p_1(M)=-\frac{1}{8\pi^2}\mathrm{tr}\,\mathcal R^2=-\frac1{8\pi^2}\mathcal R_{\alpha\beta}\mathcal R_{\beta\alpha},\qquad p_2(M)=\frac{1}{128\pi^4}\big[(\mathrm{tr}\,\mathcal R^2)^2-2\,\mathrm{tr}\,\mathcal R^4\big]=\Big(\frac1{2\pi}\Big)^4\det\mathcal R.$$

$p_2(M)$ vanishes identically *as an 8-form on a 4-manifold*, but is still useful algebraically: it equals $e(M)\wedge e(M)$ — feeding directly into the Euler class below.

### 5.4 Euler class

For $M$ a $2l$-dimensional, **orientable** Riemannian manifold (structure group $SO(2l)$), the **Euler class** $e(M)$ is the curvature-built "square root" of the top Pontryagin class, $e(A)\cdot e(A)=p_l(A)$, made precise via the **Pfaffian**. For a $2l\times2l$ skew-symmetric $A$, $\det A=\mathrm{Pf}(A)^2$ where

$$\mathrm{Pf}(A)=\frac{(-1)^l}{2^ll!}\sum_P\mathrm{sgn}(P)\,A_{P(1)P(2)}A_{P(3)P(4)}\cdots A_{P(2l-1)P(2l)}.$$

Key facts: $\mathrm{Pf}(X^tAX)=\mathrm{Pf}(A)\det X$ (giving $\det A=\mathrm{Pf}(A)^2$ for **any** skew $A$); $\mathrm{Pf}(A)$ is $SO(2l)$-invariant but flips sign under an improper rotation; and odd-dimensional skew matrices always have $\det=0$, so $e(M)\equiv0$ when $M$ is odd-dimensional.

$$\boxed{e(M)=\mathrm{Pf}(\mathcal R/2\pi)=\frac{(-1)^l}{(4\pi)^ll!}\sum_P\mathrm{sgn}(P)\,\mathcal R_{P(1)P(2)}\cdots\mathcal R_{P(2l-1)P(2l)}.}$$

**Worked example ($M=S^2$):** with $\mathcal R_{\theta\phi}=\sin\theta\,d\theta\wedge d\phi$,

$$e(S^2)=\frac{1}{2\pi}\sin\theta\,d\theta\wedge d\phi,\qquad \int_{S^2}e(S^2)=2=\chi(S^2).$$

**Worked example (4-dim $M$):** $e(M)=\frac{1}{2(4\pi)^2}\epsilon^{ijkl}\mathcal R_{ij}\wedge\mathcal R_{kl}$, with $p_2(M)=e(M)\wedge e(M)$ holding as a genuine matrix identity. **Torus $T^2$:** admits a flat connection $\Rightarrow\mathcal R=0\Rightarrow e(T^2)\equiv0=\chi(T^2)$. ✓.

### 5.5 Gauss–Bonnet theorem

$$\boxed{\int_Me(M)=\chi(M)}\qquad\text{for compact orientable }M\ (\text{both vanish if }M\text{ is odd-dimensional}).$$

This is the prototype result of the whole chapter: a purely *local* (curvature) quantity, integrated, reproduces a purely *global* (topological) invariant.

---

## 6. Hirzebruch $L$-polynomial and the $\hat A$-genus

### 6.1 $L$-polynomial and the signature theorem

$$L(x)=\prod_jx_j/\tanh x_j=1+\tfrac13p_1+\tfrac1{45}(-p_1^2+7p_2)+\tfrac1{945}(2p_1^3-13p_1p_2+62p_3)+\cdots,\qquad L(E\oplus F)=L(E)\wedge L(F).$$

**Hirzebruch signature theorem.** For $M$ a compact connected orientable 4-manifold, the intersection form $\sigma([\alpha],[\beta])=\int_M\alpha\wedge\beta$ on $H^2(M;\mathbb R)$ is symmetric and non-degenerate with $p$ positive, $q$ negative eigenvalues. The **signature** $\tau(M)\equiv p-q$ satisfies

$$\boxed{\tau(M)=\int_ML_1(M)=\frac13\int_Mp_1(M).}$$

This links a purely algebraic-topological invariant (signature of the cup-product form) to a curvature integral.

### 6.2 $\hat A$-genus (Dirac genus)

$$\hat A(\mathcal F)=\prod_j\frac{x_j/2}{\sinh(x_j/2)}=1-\tfrac1{24}p_1+\tfrac1{5760}(7p_1^2-4p_2)+\cdots,\qquad \hat A(E\oplus F)=\hat A(E)\wedge\hat A(F).$$

The $\hat A$-genus governs the **index of the Dirac operator** (Atiyah–Singer) and shows up directly in gravitational-anomaly computations.

---

## 7. Chern–Simons Forms

### 7.1 Definition via transgression

Any characteristic $2j$-form $P_j(\mathcal F)$ is closed, hence locally exact (Poincaré's lemma): $P_j(\mathcal F)=dQ_{2j-1}(\mathcal A,\mathcal F)$. This *cannot* be made global on a closed manifold without trivializing all characteristic numbers, so $Q$ only exists patch-by-patch. Explicitly, from the transgression formula of §1.4 (with $\mathcal A'=\mathcal A$, $\mathcal A_0'=0$):

$$Q_{2j-1}(\mathcal A,\mathcal F)=TP_j(\mathcal A,0)=j\int_0^1\tilde P_j(\mathcal A,\mathcal F_t,\dots,\mathcal F_t)\,dt,\qquad \mathcal F_t=t\,d\mathcal A+t^2\mathcal A^2.$$

This is the **Chern–Simons form** of $P_j$.

### 7.2 Chern–Simons form of the Chern character

With $\mathcal A_t=t\mathcal A$, $\mathcal F_t=t\mathcal F+(t^2-t)\mathcal A^2$:

$$Q_{2j-1}(\mathcal A,\mathcal F)=\frac{1}{(j-1)!}\Big(\frac i{2\pi}\Big)^j\int_0^1dt\,\mathrm{str}(\mathcal A,\mathcal F_t^{\,j-1}).$$

Lowest cases:

$$Q_1=\frac i{2\pi}\mathrm{tr}\,\mathcal A,\qquad \boxed{Q_3=\tfrac12\Big(\frac i{2\pi}\Big)^2\mathrm{tr}\Big(\mathcal A\,d\mathcal A+\tfrac23\mathcal A^3\Big)},\qquad Q_5=\tfrac16\Big(\frac{i}{2\pi}\Big)^3\mathrm{tr}\Big[\mathcal A(d\mathcal A)^2+\tfrac32\mathcal A^3d\mathcal A+\tfrac35\mathcal A^5\Big].$$

$Q_3$ is exactly $K$ from §II.5.4, and $\mathrm{ch}_2=dQ_3$ in components reproduces the familiar statement that the topological $\theta$-term density is a total divergence of the Chern–Simons current:

$$\mathrm{tr}[\epsilon^{\kappa\lambda\mu\nu}\mathcal F_{\kappa\lambda}\mathcal F_{\mu\nu}]=\partial_\kappa\Big[2\epsilon^{\kappa\lambda\mu\nu}\mathrm{tr}\big(\mathcal A_\lambda\partial_\mu\mathcal A_\nu+\tfrac23\mathcal A_\lambda\mathcal A_\mu\mathcal A_\nu\big)\Big].$$

### 7.3 Cartan's homotopy formula

For $\mathcal A_t=\mathcal A_0+t(\mathcal A_1-\mathcal A_0)$, $\mathcal F_t=d\mathcal A_t+\mathcal A_t^2$, define an antiderivation $l_t$ by $l_t\mathcal A_t=0$, $l_t\mathcal F_t=\delta t\,(\mathcal A_1-\mathcal A_0)$, extended via $l_t(\eta_p\omega_q)=(l_t\eta_p)\omega_q+(-1)^p\eta_p(l_t\omega_q)$. Using the Bianchi identity $\mathcal D_t\mathcal F_t=0$, one shows for **any** polynomial $S(\mathcal A,\mathcal F)$:

$$(dl_t+l_td)\,S(\mathcal A_t,\mathcal F_t)=\delta t\,\frac{\partial S}{\partial t}(\mathcal A_t,\mathcal F_t).$$

Integrating over $t\in[0,1]$ gives **Cartan's homotopy formula**:

$$\boxed{S(\mathcal A_1,\mathcal F_1)-S(\mathcal A_0,\mathcal F_0)=(dk_{01}+k_{01}d)\,S(\mathcal A_t,\mathcal F_t)},\qquad k_{01}S(\mathcal A_t,\mathcal F_t)\equiv\int_0^1\delta t\,l_tS(\mathcal A_t,\mathcal F_t).$$

Applying this to $S=\mathrm{ch}_{j+1}(\mathcal F)$ (closed, so the $dk_{01}d$ term drops) with $\mathcal A_1=\mathcal A,\mathcal A_0=0$ reproduces the same Chern–Simons form $Q_{2j+1}$ found directly in §7.1 — a consistency check.

### 7.4 Gauge transformation of the Chern–Simons form

$P(\mathcal F)$ is gauge invariant, but its Chern–Simons "potential" $Q$ is **not**. Under $\mathcal A\to\mathcal A^g=g^{-1}(\mathcal A+d)g$, $\mathcal F\to\mathcal F^g=g^{-1}\mathcal Fg$, Cartan's formula gives

$$\boxed{Q_{2j+1}(\mathcal A^g,\mathcal F^g)-Q_{2j+1}(\mathcal A,\mathcal F)=Q_{2j+1}(g^{-1}dg,0)+d\alpha_{2j}},$$

where the "pure gauge" term $Q_{2j+1}(g^{-1}dg,0)=(-1)^j\frac{j!}{(2j+1)!}\big(\frac{i}{2\pi}\big)^{j+1}\mathrm{tr}[(g^{-1}dg)^{2j+1}]$ is closed but only *locally* exact, and $\alpha_{2j}$ is an explicit exact correction (e.g. $\alpha_2=-\tfrac12(i/2\pi)^2\mathrm{tr}(v\mathcal A)$, $v\equiv dg\cdot g^{-1}$).

> **Physical meaning:** the Chern–Simons action shifts by a winding-number term under large gauge transformations — the geometric origin of **level quantization** in Chern–Simons gauge theory and of Wess–Zumino–Witten terms.

### 7.5 Physical application: topological mass in 3D

In 3D spacetime, a $U(1)$ gauge theory can acquire a gauge-invariant mass via the Chern–Simons term (Jackiw–Templeton; Deser–Jackiw–Templeton):

$$\mathcal L=-\tfrac14F_{\mu\nu}F^{\mu\nu}+\tfrac14m\,\epsilon^{\lambda\mu\nu}F_{\lambda\mu}A_\nu.$$

The second term is (up to normalization) exactly $Q_3(A,F)$ in components. Under $A_\mu\to A_\mu+\partial_\mu\theta$, $\mathcal L$ shifts only by a total derivative, which drops out of the action if $F$ falls off at infinity — gauge invariance survives *despite $A$ appearing explicitly*, not just through $F$.

The field equation $\partial_\mu F^{\mu\nu}+m\,{*}F^\nu=0$ implies $\partial_\mu{*}F^\mu=0$; differentiating once more gives

$$\boxed{(\partial^\lambda\partial_\lambda+m^2)\,{*}F_\kappa=0,}$$

a Klein–Gordon equation: ${*}F_\kappa$ is a genuinely **massive** vector field of mass $m$. The topological (Chern–Simons) term gives the gauge field mass *without* a Higgs mechanism.

---

## 8. Stiefel–Whitney Classes

Unlike every class above, $w_r\in H^r(M;\mathbb Z_2)$ **cannot** be built from curvature — it is discrete, mod-2 information invisible to any continuous construction. It controls orientability and the existence of spin structures.

### 8.1 Spin bundles

For $TM$ ($\dim M=m$) with structure group $O(m)$ (reducible to $SO(m)$ if orientable), the frame bundle $LM$ has transition functions $t_{ij}\in O(m)$ satisfying $t_{ij}t_{jk}t_{ki}=I$. A **spin structure** is a lift $\tilde t_{ij}\in\mathrm{Spin}(m)$ with $\varphi(\tilde t_{ij})=t_{ij}$ ($\varphi:\mathrm{Spin}(m)\to SO(m)$ the double cover) **and** $\tilde t_{ij}\tilde t_{jk}\tilde t_{ki}=I$ — note this lifted cocycle condition is **not automatic**, since $\varphi$ is two-to-one. $M$ "admits a spin structure" if such a consistent lift exists.

### 8.2 Čech cohomology with $\mathbb Z_2$ coefficients

$\mathbb Z_2=\{-1,+1\}$ (multiplicative). A **Čech $r$-cochain** $f(i_0,\dots,i_r)\in\mathbb Z_2$ is defined on non-empty overlaps $U_{i_0}\cap\cdots\cap U_{i_r}$, totally symmetric in its indices. Coboundary:

$$(\delta f)(i_0,\dots,i_{r+1})=\prod_jf(i_0,\dots,\hat i_j,\dots,i_{r+1})\quad(\text{omit index }i_j,\text{ multiply over all }j).$$

One checks $\delta^2=1$. Cocycles $Z^r=\ker\delta$, coboundaries $B^r=\mathrm{im}\,\delta$, **Čech cohomology** $\check H^r(M;\mathbb Z_2)=Z^r/B^r$.

### 8.3 First Stiefel–Whitney class — obstruction to orientability

With local orthonormal frames $e_{i\alpha}=t_{ij}e_{j\alpha}$, define the 1-cochain $f(i,j)\equiv\det(t_{ij})=\pm1$. The cocycle condition forces $\delta f=1$, so $f\in Z^1(M;\mathbb Z_2)$, defining $w_1(M)\equiv[f]\in H^1(M;\mathbb Z_2)$ (frame-independent).

> **Theorem 11.6.** $M$ is orientable $\iff w_1(M)$ is trivial.

### 8.4 Second Stiefel–Whitney class — obstruction to a spin structure

Assume $M$ orientable, $t_{ij}\in SO(m)$, lifted locally to $\tilde t_{ij}\in\mathrm{Spin}(m)$. Since $\varphi(\tilde t_{ij}\tilde t_{jk}\tilde t_{ki})=t_{ij}t_{jk}t_{ki}=I$, the product $\tilde t_{ij}\tilde t_{jk}\tilde t_{ki}\in\ker\varphi=\{\pm I\}$. Define the 2-cochain $f$ by $\tilde t_{ij}\tilde t_{jk}\tilde t_{ki}=f(i,j,k)I$; this is symmetric and closed, defining $w_2(M)\equiv[f]\in H^2(M;\mathbb Z_2)$, independent of the choice of lift.

> **Theorem 11.7.** $M$ admits a spin structure $\iff w_2(M)$ is trivial.

### 8.5 Worked examples

| Manifold | $w_1$ | $w_2$ |
|---|---|---|
| $\mathbb{C}P^m$ | $1$ (always orientable) | $1$ if $m$ odd; $x$ (generator of $H^2$) if $m$ even — **spin iff $m$ odd** |
| $S^m$ | $1$ | $1$ — always orientable and always spin |
| $\Sigma_g$ (genus-$g$ surface) | $1$ | $1$ — orientable and spin |

---

## 9. Putting It All Together: the Class Zoo

| Class | Bundle type | Built from $\mathcal F$ as | Lives in | Main use |
|---|---|---|---|---|
| Chern class $c(\mathcal F)$ | complex, $G\subset GL(k,\mathbb C)$ | $\det(I+i\mathcal F/2\pi)$ | $H^{\mathrm{even}}(M;\mathbb R)$ | classify complex bundles; monopole/instanton numbers |
| Chern character $\mathrm{ch}(\mathcal F)$ | complex | $\mathrm{tr}\exp(i\mathcal F/2\pi)$ | $H^{\mathrm{even}}(M;\mathbb R)$ | index theorems; turns $\otimes,\oplus$ into $\cdot,+$ |
| Todd class $\mathrm{Td}(\mathcal F)$ | complex | $\prod x_j/(1-e^{-x_j})$ | $H^{4\cdot}(M;\mathbb R)$ | Riemann–Roch / index theorem |
| Pontryagin class $p(\mathcal F)$ | real, $G\subset O(k)$ | $\det(I+\mathcal F/2\pi)$ | $H^{4\cdot}(M;\mathbb R)$ | tangent bundles; $p_j=(-1)^jc_{2j}$ of complexification |
| Euler class $e(\mathcal F)$ | real, oriented, rank $2l$ | $\mathrm{Pf}(\mathcal F/2\pi)$ | $H^{2l}(M;\mathbb R)$ | Gauss–Bonnet: $\int e=\chi(M)$ |
| Hirzebruch $L$ | real | $\prod x_j/\tanh x_j$ | $H^{4\cdot}(M;\mathbb R)$ | signature theorem |
| $\hat A$-genus | real | $\prod (x_j/2)/\sinh(x_j/2)$ | $H^{4\cdot}(M;\mathbb R)$ | Dirac index theorem |
| Stiefel–Whitney $w_r$ | real | *(no curvature formula!)* | $H^r(M;\mathbb Z_2)$ | $w_1$: orientability; $w_2$: spin structure |

All curvature-based classes come from exactly one machine (Chern–Weil, §1): invariant polynomial on $\mathfrak g$ $\to$ evaluate on curvature $\to$ closed, connection-independent cohomology class. Chern–Simons forms (§7) are the "antiderivatives" of all of these — gauge-dependent but with universal, controlled gauge-transformation behaviour — and are central to anomalies and topologically massive gauge theories. Stiefel–Whitney classes are the one genuinely discrete invariant in the chapter.

---

## 10. Glossary (Chapter 11 quick reference)

- **Invariant polynomial $P$** — degree-$r$ polynomial on $\mathfrak g$ with $P(g^{-1}Ag)=P(A)$; built from sums of products of $\mathrm{tr}(A^r)$.
- **Polarization $\tilde P$** — the symmetric multilinear form recovering $P$ on the diagonal.
- **Chern–Weil theorem** — $P(\mathcal F)$ is closed, and connection-independent up to an exact form (the **transgression**).
- **Characteristic class $\chi_E(P)$** — the cohomology class of $P(\mathcal F)$; vanishes on trivial bundles (obstruction to triviality).
- **Weil homomorphism** — $\chi_E:I^*(G)\to H^*(M)$ is a ring homomorphism.
- **Chern class $c(\mathcal F)=\det(I+i\mathcal F/2\pi)$** — for complex bundles; Whitney sum $\to$ product.
- **Splitting principle** — pretend any bundle is a sum of line bundles for the purpose of computing characteristic classes.
- **Classifying space $G_k(\mathbb C)$ / universal bundle $L_k$** — bundles over $M$ $\leftrightarrow$ homotopy classes of maps $M\to G_k(\mathbb C)$.
- **Chern character $\mathrm{ch}(\mathcal F)=\mathrm{tr}\exp(i\mathcal F/2\pi)$** — turns both $\oplus$ and $\otimes$ into simple algebra; key to Atiyah–Singer.
- **Todd class** — extra ingredient in Riemann–Roch/index theorems for complex (Dolbeault) bundles.
- **Pontryagin class $p(\mathcal F)=\det(I+\mathcal F/2\pi)$** — for real bundles; related to Chern classes of the complexified bundle.
- **Pfaffian / Euler class** — "square root" of the top Pontryagin class; Gauss–Bonnet theorem $\int_Me(M)=\chi(M)$.
- **Hirzebruch $L$-polynomial** — governs the signature theorem $\tau(M)=\frac13\int p_1(M)$.
- **$\hat A$-genus (Dirac genus)** — governs the index of the Dirac operator.
- **Chern–Simons form $Q_{2j-1}$** — local antiderivative of a characteristic class, $P_j=dQ_{2j-1}$; gauge-dependent but with controlled transformation law; gives topological mass terms in odd dimensions.
- **Cartan's homotopy formula** — the tool used to derive transgressions and gauge-variation formulas systematically.
- **Spin structure** — a consistent lift of $TM$'s transition functions to $\mathrm{Spin}(m)$.
- **Stiefel–Whitney classes $w_1,w_2$** — $\mathbb Z_2$-valued obstructions to orientability and to the existence of a spin structure, respectively; not curvature-expressible.


---

## 11. How the Three Chapters Fit Together

| Stage | Chapter | Core object | Key payoff |
|---|---|---|---|
| 1 | 9 — Fibre Bundles | transition functions $t_{ij}$ valued in $G$ | a bundle's twisting is entirely gluing data; trivial $\iff$ global section |
| 2 | 10 — Connections | connection 1-form $\omega$, curvature $\Omega=\mathcal D\omega$ | curvature = local field strength; holonomy = Wilson loop/Berry phase; flat $\ne$ trivial holonomy |
| 3 | 11 — Characteristic Classes | invariant polynomial $P(\mathcal F)$ | curvature integrals are quantized, connection-independent topological invariants that *prove* non-triviality |

The integers that kept appearing by hand in Chapter 10 — monopole charge $n=\frac{i}{2\pi}\oint\mathcal F$, instanton number $n=-\frac1{8\pi^2}\int\mathrm{tr}\,\mathcal F^2$, Berry-phase "monopole charge" at a level crossing — are now seen to be specific evaluations of universal polynomials in the curvature: $\mathrm{ch}_1$ for the monopole, $\mathrm{ch}_2$ (equivalently $c_2$) for the instanton. The Euler class generalizes the Gauss–Bonnet integer $\chi(M)$ the same way the Chern class generalizes the monopole/instanton integers. And the Stiefel–Whitney classes answer a question Chapters 9–10 could only gesture at: *which manifolds even admit the structures (orientations, spinors) that the rest of the machinery silently assumes?*

> **Final big-picture sentence:** A fibre bundle's *existence* (Ch. 9) is gluing data; its *dynamics* (Ch. 10) is curvature; its *topology* (Ch. 11) is what curvature integrates to — and that's the whole arc of "geometry $\to$ physics" running through Yang–Mills theory, monopoles, instantons, anomalies, and the index theorem.
