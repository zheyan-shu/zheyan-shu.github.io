# An Aside: Quantum Computing

## Some Conventions

$$X = \begin{bmatrix}
        0 & 1\\
        1 & 0\\
    \end{bmatrix}
    \quad
    Y = \begin{bmatrix}
        0 & -i\\
        i & 0\\
    \end{bmatrix}
    \quad
    Z = \begin{bmatrix}
        1 & 0\\
        0 & -1\\
    \end{bmatrix}$$ 
    The spin lowing and raising operators are defined by

$$\sigma^- = \frac{1}{2}(X-iY) \quad \sigma^+ = \frac{1}{2}(X+iY)$$

## Quantum Error Correction

### Parent Hamiltonian

Parent Hamiltonian defines an energy framework that ground state
represents error-free states. In the case of a three-qubit repetition
code, the parent Hamiltonian is

$$

    H = -J(Z_1Z_2+Z_2Z_3)

$$

where $Z_1Z_2$ and $Z_2Z_3$ are called *stabilizers*.

### Ground states

There is a two-fold degeneracy of ground states, denoted as
$\ket{0}=\ket{000}$ and $\ket{1}=\ket{111}$ Any derivation of ground
states would increase the energy of this system.

### Logical operators

Logical operators are defined such that they are non-trivial map on the
code space. They are defined by modulo out stabilizers, which implies if
two logical operators differ from each other only by a multiplication of
stablizers, they are equivalent. In our case, 

$$

    \begin{aligned}
        \bar{X} = X_1X_2X_3 : \bar{X}\ket{0} = \ket{1} \quad \bar{X}\ket{1} = \ket{0} \\
        \bar{Z} = Z_i : \bar{Z}\ket{0} = \ket{0} \quad \bar{Z}\ket{1} = -\ket{1}\\
    \end{aligned}

$$

::: tcolorbox
Stabilizers are defined to construct Hamiltonian, while logical
operators are those commute with stabilizers but acts non-trivially on
code space. The minimal Pauli weight of logical operators is called
*code distance* of a quantum code.
:::

# 1D topological phenomena

We study two mathematically equivalent models, *transver field Ising
model* and *Kitaev chain*. It can be shown using *Jordan-Wigner
transformation* the two models can be mapped from one to the other.

## AKLT Model

AKLT model, named after Affleck-Kennedy-Lieb-Tasaki, is defined by
following Hamiltonian 

$$

    H = \sum_i\left[\vec{S}_i\cdot\vec{S}_{i+1} + \frac{1}{3} (\vec{S}_i\cdot\vec{S}_{i+1})^2\right]

$$ 

The exact form could be thought as any two adjacent
spin-1 There is a non-local transform

# Berry Curvature

Consider a Hamiltonian with parameters varying slowly with time,
$\vec{R}(t)$. Those parameters could be external magnetic fields,
electric fields and so on. Since the system is changed adiabatically, we
assume that an eigenstate would remain to be instaneous eigenstate as
parameters running up to a phase factor. We define the energy eigenstate
in the paramter space as 

$$

    H(\vec{R})\ket{n(\vec{R})} = E_n(\vec{R})\ket{n(\vec{R})}

$$ 

Therefore we write the evolving state as

$$

    \ket{\psi(t)} = e^{-\theta(t)}\ket{n(\vec{R}(t))}

$$ 

Compute the Shrödinger equation with adiabatic ansatz,
we find the differential equation satisfied by phase factor,

$$

    E_n(\mathbf{R}(t))-i \hbar\langle n(\mathbf{R}(t))| \frac{d}{d t}|n(\mathbf{R}(t))\rangle=\hbar \frac{d \theta(t)}{d t} .

$$ 

Integrate with time, we find there are two different
contribution, one comes entirely from dynamical evolution, the other
arises from the geometry of parameter space. We are mostly intereted in
the second one, which is so-called *Berry phase*. 

$$

    \gamma_n = i\int_0^t dt' \bra{n(\vec{R}(t'))}\frac{d}{dt'}\ket{n(\vec{R}(t'))}

$$ 

This motivates the definition of *Berry connection*,
which is defined as a one-form on the parameter space of the quantum
system. 

$$

    \mathbf{A}_n(\mathbf{R}) = i\bra{n(\mathbf{R})}\nabla_{\mathbf{R}}\ket{n(\mathbf{R})}

$$ 

Clearly, this is not gauge-invariant, where we have
defined the gauge transform as the arbitrary phase choice of the
eigenstates, and the story is the same as we encounter in the
electromagnetism. One could show that the Berry phase could be written
in terms of Berry connection in a compact form, 

$$
    \gamma_n = \oint_{\mathcal{C}} \mathbf{A}_n(\mathbf{R})\cdot d\mathbf{R}
$$ 

where we have assumed that we return to the same point
in the parameter space. By Stoke's theorem, we may define *Berry curvature* if the space is three-dimensional, which could also be thought as the field strength, given that Berry connection being a gauge
potential.

A further computation shows that Berry phase could be put into a
computationally convenient form, that is, we may compute it with
derivatives of Hamiltonian in stead of derivatives of states.

$$
    \gamma_n = -\int_{\mathcal{S}}d\mathbf{S}\cdot \mathbf{V}_n
$$ 

where $\mathbf{V}_n$ is defined as 

$$
    \mathbf{V}_n = \operatorname{Im}\sum_{m\neq n}\frac{\bra{n(\mathbf{R})}(\nabla_R H)\ket{n(\mathbf{R})} \bra{n(\mathbf{R})}(\nabla_R H)\ket{m(\mathbf{R})}}{(E_m(\mathbf{R})-E_n(\mathbf{R}))^2}
$$ 

that is related with Berry curvature via
$V_{ni} = \epsilon_{ijk}F_{jk}$.

## A two-level system

Consider following Hamiltonian 

$$
    H = \mathbf{d}(\mathbf{R})\cdot \sigma
$$ 

we have ignored contribution from identity matrix as it
only shifts enegies by a constant. We parametrized $\mathbf{d}$ in
spherical coordinate 

$$

    \mathbf{d}(\mathbf{R}) = |{d}|(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)

$$ 

A convenient choice of eigenstates with energies
$\pm |d|$ is 

$$

    \ket{+\mathbf{R}} = 
    \begin{pmatrix}
        \cos\frac{\theta}{2}\\
        \sin\frac{\theta}{2}e^{i\phi}
    \end{pmatrix}
    \quad
    \ket{-\mathbf{R}} = 
    \begin{pmatrix}
        \sin\frac{\theta}{2}e^{-i\phi}\\
        -\cos\frac{\theta}{2}
    \end{pmatrix}

$$ 

However, such choice of eigenstates is not well-defined
globally. That is, at the south pole where $\theta = \pi$, eigenstates may vary as $\phi$ changes, indicating a singularity. This would not
make any problme as we know from differential geometry this can be
resolved by gluing different patches on the two-sphere. The Berry
curvature is easy to compute and one can show it takes the same form
even we change from one patch to the other, 

$$

    F_{\theta\phi} = \frac{1}{2}\sin\theta.

$$

Generally, if we take the Cartesian coordinate system and choose
$\mathbf{d} = \mathbf{R}$. Then $H = x\sigma_x+y\sigma_y+z\sigma_z$.
Assume that at a specific time, $\mathbf{R}$ is along z-direction and
choose eigenstates to be the usual ones, satisfying 

$$

    \sigma_z\ket{+} = \ket{+} \quad \sigma_z\ket{-} = -\ket{-}

$$ 

Then $\mathbf{V}_+$ is computed by

# The Integer Quantum Hall Effect

In this section, we would like to discuss *the integer quantum Hall effect* first.

## Laudau levels

[Briefly discuss Laudau levels]{style="color: blue"}

## General arguments

Quantum Hall effect is that one finds that a material's Hall resistivity
takes special value 

$$

    \rho_{xy} = \frac{2\pi\hbar}{e^2} \frac{1}{\nu} \quad \nu\in \mathbb{Z}

$$ 

If we compare this result with the classical
calculation in Drude model, in which the resistivity is found to be,

$$

    \rho_{xy} = \frac{B}{ne}

$$ 

where $B$ is the external magnetic field and $n$ is the
electron density, one readily finds that on the $\nu$-th plateau,

$$

    n = \frac{B}{\Phi_0}\nu

$$ 

where $\Phi_0 = \frac{2\pi\hbar}{e}$ is the flux
quantum in the usual sense. Let us first make a comment on this
calculation.

Indeed, this is value of magnetic field we find on the center of the
plateau, however not enough to explain the existence of plateau. What
would happen when we move away from the specific value of magnetic
field? Given that the material is pure, there is no where for electrons
to go if we assume $k_\mathrm{B}T \ll \hbar \omega_B$, where
$\hbar\omega_B$ is the energy gap between two different Laudau levels.
Actually, this is a result of impurity of materials, thus somewhere
*disorder* should be taken into account.

#### The role of disorder, part I

It is quite easy to see why disorder may help us to solve this problem.
Mathematically, we introduce a random potential to the Hamlitonian,
which effectively model the effect of disorder. We further require that
the impurity is not that much, so that the typical value of the random
potential is much smaller compared with the gap, 

$$

    V \ll \hbar\omega_B.

$$ 

Intuitively, this potential would not change the
behaviour of Laudau level significantly, that is, the center of each
Laudau level would not shift, at least the leading order of such
perturbation. However, degenerate states would split due to such general
perturbation, since they do not preserve any symmetry of original
Hamiltonian. See fig [1](#fig:tong_fig1){reference-type="ref"
reference="fig:tong_fig1"} for an illustration.

<figure id="fig:tong_fig1" data-latex-placement="H">
<img src="tong_fig1.png" style="width:80.0%" />
<figcaption>States in the presence of disorder</figcaption>
</figure>

#### The role of disorder, part II

On the other hand, such random potential may take *extended states* into
*localized states*, since impurity would prevent a electron from moving
far away from its original position. We can easily see the emergence of
localized states at the classical level. We assume that

$$

    |\nabla V| \ll \frac{\hbar\omega_B}{l_B}

$$ 

where $l_B$ is the magnetic radius. Recall that if we
use the symmetric gauge, states could be labelled by the center of the
orbit $(X,Y)$. One could again compute the commutator of them with the
full Hamiltonian, 

$$

    \begin{aligned}
        i \hbar \dot{X} & =[X, H+V]=[X, V]=[X, y] \frac{\partial V}{\partial y}=i l_B^2 \frac{\partial V}{\partial y} \\
        i \hbar \dot{Y} & =[Y, H+V]=[Y, V]=[Y, x] \frac{\partial V}{\partial x}=-i l_B^2 \frac{\partial V}{\partial x}
\end{aligned}

$$ 

which means the center would move along the direction
of equipotentials. So why this means we have localized states and
extended states? First, it is easily to see states are extended without
random potential as one can solve the wave function for each Laudau
level and in the Laudau gauge the translation symmetry along
$y$-direction means they are extended along this direction. Second, in
the existence of random potential we may assume there are local maximums
and local minimums. States near those extrimums could only move near
them, as they have been trapped close to extremums due to the force of
random potential. And states that have medium energy could move along
equipotentials that expand largely in the space, thus being referred to
extended states. See fig [2](#fig:tong_fig2){reference-type="ref"
reference="fig:tong_fig2"} for an illustration.

<figure id="fig:tong_fig2" data-latex-placement="ht">
<img src="tong_fig2.png" style="width:80.0%" />
<figcaption>Localized states and extended states</figcaption>
</figure>

Intuitively, only extended states can transport charge from one side of
material to the other. Then as we fill all the extended states in a
given Laudau level and decrease the magnetic field $B$, each Laudau
level can accomodate fewer states. However rather than jump to the next
Laudau level directly, states change from extended ones to localized
ones. That is, we have a plateau before localised states are also fully
filled and we may jump to the next plateau.

## Topology associated with quantum Hall effect

In this subsection, we would like to relate the quantum Hall effect with
topology.

The first one we would like to derive is the *Kubo formula*, which
relates the Hall conductity with quantum observables and is part of
*linear response*.

Consider a general Hamiltonian $H_0$ with energy eigenstates
$H_0\ket{n} = E_n\ket{n}$. We would like to add a background electric
field and work in the gauge $A_0=0$. The electric field is
$\mathbf{E} = -\partial_t \mathbf{A}$ and electrons are coupled with
this by adding an extra term $\Delta H = -\mathbf{J}\cdot\mathbf{A}$ to
the Hamiltonian. We would like to consider DC field however work with an
occillating field. That is we take
$\mathbf{E}(t) = \mathbf{E} e^{-i\omega t}$ first and take $\omega\to 0$
at the end of our calculation. For such a electric field, the gauge
potential is given by
$\mathbf{A} = \frac{\mathbf{E}}{i\omega}e^{-i\omega t}$. Our goal is to
compute the current $\b{\mathbf{J}(t)}$ induced in this
circumstance.

We would like to work in the interacting picture, where operators evolve
as $\mathcal{O}(t)=e^{iH_0t/\hbar}\mathcal{O}(0)e^{-iH_0t/\hbar}$ and
states evolve by 

$$

    \ket{\psi(t)}_I = U(t,t_0)\ket{\psi(t_0)}_I

$$ 

where the evolution operator is defined as

$$

    U(t,t_0) = \operatorname{T}\exp(-\frac{i}{\hbar}\int_{t_0}^tdt' \Delta H(t'))

$$ 

where $\operatorname{T}$ stands for the time ordering.
The computation is staightford. Suppose that we prepare our state in the
many-body ground state $\ket{0}$ in the far-past, 

$$

    \begin{aligned}
        \langle{\mathbf{J}(t)\rangle} &= \bra{0(t)}\mathbf{J}(t)\ket{0(t)} \\ 
        & = \bra{0}U^{-1}(t)\mathbf{J}(t)U(t)\ket{0} \\
        & \approx \bra{0}\mathbf{J}(t) + \frac{i}{\hbar}\int_{-\infty}^{t}dt' [\Delta H(t'), \mathbf{J}(t)]\ket{0}
    \end{aligned}

$$ 

where $U(t)$ is the abbreviation of evolution operator
from past-infinity to $t$ and we have already expand $U(t)$ to leading
order in the last step. Each component can be shown to be brought to
following form 

$$

    \braket{J_i(t)}=-\frac{1}{\hbar \omega}\left(\int_0^{\infty} d t^{\prime \prime} e^{i \omega t^{\prime \prime}}\langle 0|\left[J_j(0), J_i\left(t^{\prime \prime}\right)\right]|0\rangle\right) E_j e^{-i \omega t}.

$$ 
From the above formula, it is clear that the diagonal
component of condutivity is $0$ and the off-diagonal components is

$$

    \sigma_{xy}(\omega) = -\frac{1}{\hbar \omega}\left(\int_0^{\infty} d t e^{i \omega t}\langle 0|\left[J_j(0), J_i\left(t\right)\right]|0\rangle\right).

$$ 

This is the *Kubo formula* of Hall conductivity. Use
the evolution of current operator we mentioned above, this could be
expanded using the eigenstates of $H_0$ and perform the integral over
$\int dt$, where an extra small imaginary part should be introduced to
make the integral convergent, $\omega \to \omega + i\epsilon$. The final
result is 

$$

    \sigma_{xy}(\omega) = \frac{i}{\omega}\sum_{n\neq 0} \frac{\bra{0}J_y\ket{n}\bra{n}J_x\ket{0}}{E_n - E_0 + \hbar \omega } - \frac{\bra{0}J_x\ket{n}\bra{n}J_y\ket{0}}{\hbar \omega-E_n + E_0}.

$$ 

Expand around $\omega\to 0$ and throw away the
divergent part(which would be important for the longitudinal
conductivity however we are not going to discuss it here), we have

$$

    \sigma_{x y}=-i \hbar \sum_{n \neq 0} \frac{\langle 0| J_y|n\rangle\langle n| J_x|0\rangle-\langle 0| J_x|n\rangle\langle n| J_y|0\rangle}{\left(E_n-E_0\right)^2}

$$

Now we are ready to discuss the topological nature of quantum Hall
effect. Let us consider the Hall system on a torus $\mathbf{T}^2$, which
can be viewed as a rectangle with opposite sites identified. First, we
can no longer impose periodic boundary condition for electrons due to
the existence of magnetic field. We introduce the *magnetic translation
operators*, 

$$

    T(\mathbf{d}) = \exp(i\mathbf{d}\cdot (-i\nabla - e\mathbf{A}/\hbar)).

$$ 

We require that the state is invariant under the
translation of the torus by the magnetic translation operators. However,
it is clear that the wave function would acquire a phase when we
translate it around a circle of the torus, which is also
gauge-dependent. If we take the Laudau gauge $A_x=0, A_y = Bx$, then
$T_x$ is the usual translation operator but
$T_y = \exp(y\partial_y - iyeBx/\hbar)$. That means when we move around
a circle along $y$-direction, the wave function would pick up a phase

$$

    T(0,L_y)\psi(x,y) = \exp(-ieBxL_y/\hbar)\psi(x,y+L_y) = \psi(x,y).

$$ 

However, we find that
$T_xT_y = \exp(-i e B L_x L_y/\hbar) T_y T_x$. That is, the two
translation operators do not commute with each other. To make them
commute, we require the factor to be a multiple of $2\pi$,

$$

    \frac{eBL_xL_y}{\hbar} = 2\pi N \quad N \in \mathbb{Z},

$$ 

which give rise to the Dirac quantization condition for
magnetic flux. It is again easy to see that we could perturb the
Hamiltonian by adding constant magnetic flux along two directions.

$$

    \begin{aligned}
        & A_x = \frac{\Phi_x}{L_x} \\
        & A_y = \frac{\Phi_y}{L_y} + Bx
    \end{aligned}

$$ 

The addition Hamiltonian is
$\Delta = - \sum\limits_{i=x,y}\frac{J_i\Phi_i}{L_i}$. Then to the first
order in the perturbation theory, the energy eigenstates ara given by

$$

    \ket{\psi_0}' = \ket{\psi_0} + \sum_{n\neq \psi_0} \frac{\bra{n}\Delta H\ket{\psi_0}}{E_n-E_0}\ket{n}

$$ 

Consider infinitesimal changes of $\Phi_i$, and we
differentiate above formula with respect to $\Phi_i$, it can be shown
that the right-handed side takes the form of Kubo formula. In all, the
Kubo formula for Hall conductivity can be written as 

$$

    \sigma_{xy} = -i\hbar \left[\frac{\partial }{\partial \Phi_y}\bra{\psi_0}\ket{\frac{\partial \psi_0}{\partial \Phi_x}} - \frac{\partial }{\partial \Phi_x}\bra{\psi_0}\ket{\frac{\partial \psi_0}{\partial \Phi_y}}\right]

$$ 

Again, we surprisingly find that it takes a very
similar form with the Berry curvature in the parameter space! If we set
$\theta_i = \frac{2\pi\Phi_i}{\Phi_0}$ being angular variables, which
should take value in $[0,2\pi)$ since the spectrum is invariant if the
magnetic flux is a multiple of flux quanta, being *spectual flow* that
we did not discuss here.

If we define the Berry connection which, in this case, lives over
$\mathbf{T}_{\Phi}^2$, by 

$$

    \mathcal{A}_i = -i \bra{\psi_0} \frac{\partial }{\partial \theta_i} \ket{\psi_0}.

$$ 

The field strength can be easily computed and can be
shown to be directly related with Hall conductivity 

$$

    \sigma_{xy} = -\frac{e^2}{\hbar}\mathcal{F}_{xy}

$$ 

To see why the Hall conductivity is quantized, one
needs to average over the parameter space 

$$

    \sigma_{xy} = -\frac{e^2}{\hbar} \int_{\mathbf{T}_{\Phi}^2}\frac{d^2\theta}{(2\pi)^2}\mathcal{F}_{xy}

$$ 

However an integral of curvature over the space is
always a integer, which is called **Chern number**. Here the Chern
number is defined by 

$$

    C = -\frac{1}{2\pi} \int_{\mathbf{T}_{\Phi}^2}\frac{d^2\theta}{(2\pi)^2}\mathcal{F}_{xy} \quad \text{and} \quad C\in\mathbb{Z}

$$ 

The Hall conductivity is thus quantized

$$

    \sigma_{xy} = \frac{e^2}{2\pi\hbar} C

$$ 

The
relation [\[eq:tknn_inv\]](#eq:tknn_inv){reference-type="eqref"
reference="eq:tknn_inv"} is so-called *TKNN invariant*.

::: tcolorbox
It seems hard to understand why we take an average over $\theta$ here
for the first time one encounter this formula. However the physics is
rahter simple. Terms used to perturb Hamiltonian can be thought as
twisted boundary conditions, which need to be averaged when we want
physical obervable conductivity.
:::

## Laughlin's argument

We briefly discuss Laughlin's argument for quantized Hall effect. We
adopt Laudau's gauge 

$$A = (0,Bx,0)$$

In this gauge, the translation symmetry in $y$-direction is preserved
and $k_y$ is a good quantum number. It can be shown that the eigenstates
of Hamiltonian is labeled by level of occillator in $x$-direction and
$k_y$. As one may compute directly, $k_y$ effectively shifts the center
of occillators in $x$-direction, $\braket{x} = -l^2 k_y$. Once we impose
periodic boundary condition in $y$-direction, $k_y$ is quantized

$$

k_y = \frac{2\pi n}{L_y}

$$

We also have a finite length in
$x$-direction, say $L_x$, then degeneracy of a Laudau level is given by

$$

N = \frac{\Delta k_y}{\delta k_y} = \frac{L_x/l^2}{2\pi/L_y} = \frac{A}{2\pi l^2} = \frac{AB}{\Phi_0}

$$

If we adiabatically increase flux in $z$-direction, which means
$A_y = Bx + \frac{\Phi}{L_y}$, then

$$

\langle x \rangle = -l^2(k_y + \frac{e\Phi}{\hbar L_y}) = -\frac{2\pi l^2}{L_y}(n + \frac{\Phi}{\Phi_0})

$$

from which we find that if we add one unit of flux, the position of
occillator is shifted from $n$ to $n+1$, and the system doesn't change
but each quantum state evovles to the next level. Thus if a Laudau level
is full filled, then such *spectral flow* would effectively translate
one state from most inner orbit to an outer orbit, meaning one electron
is moving. The Hall conductance can be read from following formula and
$\nabla\times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$

$$
Q = \int dt \oint j_r dl = \sigma_{xy}\int dt \oint E_\theta dl = -\sigma_{xy}\Delta\Phi
$$

*Aside: In this case if we label degenerate states in a given Laudau
level by $n$ where $n=0,1,\cdots,N-1$, then it is weird at first sight
where does the most outer state move. This is explained by that the
$n=N$ state is an edge state, which is not completely degenerate with
bulk states.*

## Topological insulators

So far so good, we have already explain the relation between quantized
Hall conductivity and topology. In this section, we would like to
discuss more practical models. Let us consider particles on a lattice.
The first thing that one should be awared of is that now momentum should
be restricted in *Brillouin zone*.

::: definition
**Definition 1** (Brillouin zone). *Consider that particles are living
in 1d space, that is $\mathbb{R}$, the momentum eigenfunction is given
by $e^{ikx}$ and $k$ would take value in $\mathbb{R}$. However if we
restrict ourselves to 1d lattice with lattice distance $a$, such that
partilces have quantized position $x_n=na$, then one finds that for
$\psi_k(x_n) = e^{ikna}$, this is invariant under $k\to k+G$, where
$G=\frac{2\pi}{a}$. Thus one can not tell the difference between $k$ and
$k+G$, and the momentum space should modulo out such a translation. One
may take 

$$

        k \in [-\frac{\pi}{a},\frac{\pi}{a})

$$ 

as the first Brillouin zone.*
:::

Given the definition of Brillouin zone, we consider a particle living in
a rectangular lattice, where the lattice distance are given by $a$ and
$b$ in $x$- and $y$-direction, repectively. The topology of momentum
space is a torus $\mathbf{T}^2$ as we have the identification
$k_x\sim k_x+ \frac{2\pi}{a}$ and $k_y\sim k_y+ \frac{2\pi}{b}$. In a
given band, the wave function can be brought to the Bloch form

$$

    \psi_{\mathbf{k}}(\mathbf{x}) = e^{i\mathbf{k}\cdot \mathbf{x}}u_{\mathbf{k}}(\mathbf{x})

$$ 

where $u_{\mathbf{k}}(\mathbf{x})$ is usually periodic
in a unit cell. We should make several assumptions before moving into
concrete calculation

- First, we assume that the single particle spectrum decompose into
  bands, with each band parameterized by the momentum $\mathbf{k}$ which
  lives on a torus.

- Second, we assume that particles are non-interacting, and the
  multi-particle spectrum is constructed by filling up the
  single-particle spectrum, subject to Pauli exclusion principle.

- Finally, we assume that there is a energy gap between bands and there
  exist a Fermi energy $E_F$ lives in one of these gaps. States below
  $E_F$ are fully filled while bands above $E_F$ are empty.

For each bands that below the Fermi energy, we can do the same thing as
above. For each band there exist a Berry connection defined as

$$

    \mathcal{A}_i(\mathbf{k}) = -i \bra{u_{\mathbf{k}}} \frac{\partial }{\partial k_i} \ket{u_{\mathbf{k}}}.

$$ 

Here the connection is defined in the Hilber space
itself, which is different from what we did before. Desipte of that, the
story goes in the usual sense. The Berry curvature associate with
$\mathcal{A}_i$ is 

$$

    \mathcal{F}_{x y}=\frac{\partial \mathcal{A}_y}{\partial k^x}-\frac{\partial \mathcal{A}_x}{\partial k^y}=i\left\langle\left.\frac{\partial u}{\partial k^y} \right\rvert\, \frac{\partial u}{\partial k^x}\right\rangle-i\left\langle\left.\frac{\partial u}{\partial k^x} \right\rvert\, \frac{\partial u}{\partial k^y}\right\rangle

$$ 

For each band $\alpha$ there is an associate Chern
number and the Hall conductivity is given by a summation

$$

    \sigma_{xy} = \frac{e^2}{2\pi\hbar}\sum_\alpha C_\alpha

$$

::: proof
*A brief proof of
formula [\[eq:hall_insulator\]](#eq:hall_insulator){reference-type="eqref"
reference="eq:hall_insulator"}.* The ground state is given by a tensor
of single-particle states below the Fermi surface, schematically
$\ket{\Psi_0} = \prod\limits_{E_\alpha<E_F}c_{\alpha}(\mathbf{k})^\dagger\ket{0}$.
An insertion of current operator between excited state and ground state
effectively becomes
$\bra{u_{\alpha}^\mathbf{k}}J_y\ket{u_{\beta}^\mathbf{k}}$.

Let us look at the Schödinger equation of Bloch wave function, which
reads 

$$

        \begin{aligned}
            H\left|\psi_{\mathbf{k}}\right\rangle=E_{\mathbf{k}}\left|\psi_{\mathbf{k}}\right\rangle & \Rightarrow\left(e^{-i \mathbf{k} \cdot \mathbf{x}} H e^{i \mathbf{k} \cdot \mathbf{x}}\right)\left|u_{\mathbf{k}}\right\rangle=E_{\mathbf{k}}\left|u_{\mathbf{k}}\right\rangle \\
            & \Rightarrow \tilde{H}(\mathbf{k})\left|u_{\mathbf{k}}\right\rangle=E_{\mathbf{k}}\left|u_{\mathbf{k}}\right\rangle \quad \text { with } \quad \tilde{H}(\mathbf{k})=e^{-i \mathbf{k} \cdot \mathbf{x}} H e^{i \mathbf{k} \cdot \mathbf{x}}
        \end{aligned}

$$ 

The current operator is defined in terms of the group
velocity
$\mathbf{J} = \frac{e}{\hbar} \frac{\partial \tilde{H}}{\partial \mathbf{k}}$.
One can check that this perfectly match $\mathbf{J}=e\dot{\mathbf{x}}$.
Now we are left with algebraric calculation 

$$

        \begin{aligned}
            \sigma_{xy} &= -i\hbar \sum_{E_\alpha<E_F<E_\beta}\int_{\mathbf{T}^2}\frac{d^2k}{(2\pi)^2} \frac{\bra{u_{\alpha}^\mathbf{k}}J_y\ket{u_{\beta}^\mathbf{k}}\bra{u_{\beta}^\mathbf{k}}J_x\ket{u_{\alpha}^\mathbf{k}}-\bra{u_{\alpha}^\mathbf{k}}J_x\ket{u_{\beta}^\mathbf{k}}\bra{u_{\beta}^\mathbf{k}}J_y\ket{u_{\alpha}^\mathbf{k}}}{(E_\alpha(\mathbf{k})-E_\beta(\mathbf{k}))^2} \\
            &= -i\frac{e^2}{\hbar} \sum_{E_\alpha<E_F<E_\beta}\int_{\mathbf{T}^2}\frac{d^2k}{(2\pi)^2} \frac{\bra{u_{\alpha}^\mathbf{k}}\partial_y \tilde{H}\ket{u_{\beta}^\mathbf{k}}\bra{u_{\beta}^\mathbf{k}}\partial_x \tilde{H}\ket{u_{\alpha}^\mathbf{k}}-\bra{u_{\alpha}^\mathbf{k}}\partial_x \tilde{H}\ket{u_{\beta}^\mathbf{k}}\bra{u_{\beta}^\mathbf{k}}\partial_y \tilde{H}\ket{u_{\alpha}^\mathbf{k}}}{(E_\alpha(\mathbf{k})-E_\beta(\mathbf{k}))^2} \\
            &= -i\frac{e^2}{\hbar} \sum_{E_\alpha<E_F<E_\beta}\int_{\mathbf{T}^2}\frac{d^2k}{(2\pi)^2} \braket{\partial_y u_{\alpha}^\mathbf{k}}{u_{\beta}^\mathbf{k}}\braket{u_{\beta}^\mathbf{k}}{\partial_x u_{\alpha}^\mathbf{k}}-\braket{\partial_x u_{\alpha}^\mathbf{k}}{u_{\beta}^\mathbf{k}}\braket{u_{\beta}^\mathbf{k}}{\partial_y u_{\alpha}^\mathbf{k}} \\
            &= -i\frac{e^2}{\hbar} \sum_{\alpha}\int_{\mathbf{T}^2}\frac{d^2k}{(2\pi)^2} \braket{\partial_y u_{\alpha}^\mathbf{k}}{\partial_x u_{\alpha}^\mathbf{k}}-\braket{\partial_x u_{\alpha}^\mathbf{k}}{\partial_y u_{\alpha}^\mathbf{k}}
        \end{aligned}

$$ 

Compare the integrand with the definition of Berry
curvature [\[eq:curv_chern_ins\]](#eq:curv_chern_ins){reference-type="eqref"
reference="eq:curv_chern_ins"}, we proof the
formula [\[eq:hall_insulator\]](#eq:hall_insulator){reference-type="eqref"
reference="eq:hall_insulator"}. ◻
:::

#### Chern insulators

The simplest case is following single-particle Hamiltonian (in the
momentum space) 

$$

    \tilde{H}(\mathbf{k}) = \vec{E}(\mathbf{k})\cdot \vec{\sigma} + \epsilon(\mathbf{k})\mathbf{1}

$$ 

There are only two bands, each with energy
$\epsilon(\mathbf{k})\pm E(\mathbf{k})$. For any model, we can introduce
a unit vector on the two-sphere
$\vec{n}(\mathbf{k}) = \frac{\vec{E}(\mathbf{k})}{|\vec{E}(\mathbf{k})|}$.
Clearly this induces a map from $\mathbf{T}^2\to\mathbf{S}^2$. Then the
Chern number for this system could be written as 

$$

    C = \frac{1}{4\pi}\int_{\mathbf{T}^2}k \vec{n}\cdot (\frac{\partial \vec n}{\partial k_x}\times\frac{\partial \vec n}{\partial k_y})

$$ 

This formula effectively measures how many times
$\mathbf{T}^2$ wraps around $\mathbf{S}^2$.

::: tcolorbox
Let us briefly summarize what we are studying here. For a system with a
compact space of momentum, we have a map from the Brillouin zone to
parameter space, that is

$$\phi:\mathbf{k}\mapsto \mathbf{d}(\mathbf{k}).$$ 
So if we want a non
zero Chern number, each point on the two sphere must be taken at least
once, which means $\mathbf{T}^2$ wraps $\mathbf{S}^2$.
:::

#### Lattice Chern insulators

Consider the symmetry allowed by crystal and the low energy effective
physics around small momentum region, the Hamiltonian necessarily looks
like 

$$

    H = \sin (k_x) \sigma_x + \sin (k_y) \sigma_y + B(2+M-\cos(k_x)-\cos(k_y))\sigma_z,

$$ 

to the lowest order of Fourier modes.

# Chern Insulators, Time Reversal Symmetry and Topological Insulators

*I am not sure about the physical picture of this chapter. In a sense, I
think that topological phase transition is not a good desciption of the
main idea of this chapter.\
Instead, we talk about how different mass term are related with topology
of insulators. That is, symmetry of system usually contrains possible
terms appearing in Hamiltonian, which are responsible for gap-closing in
the low energy limit. So if a certain symmetry is required, a
topological phase may be forbidden. For example, if time reversal
symmetry is required, system cannot have non-zero Chern number
generally, thus the Hall conductance is zero.\
On the other hand, it can be shown that upon maintaining time reversal
symmetry, we can still have other non-trivial topological phases that
are categorized by $\mathbb{Z}_2$ symmetry. And they are achieved by
adding different kinds of mass terms.*

## Time reversal symmetry

Generally, time reversal symmetry would protect systems from non-trivial
topological phases. For spinless systems, time reversal symmetry acting
on Bloch Hamiltonian as simply changing the sign of momentum

$$

    T h(\mathbf{k}) T^{-1} = h(-\mathbf{k})

$$ 

Then, if $\ket{\psi(\mathbf{k})}$ is an eigenstate at
momentum $\mathbf{k}$, $T\ket{\psi(\mathbf{k})}$ is an eigenstate at
$-\mathbf{k}$.

## Other kinds of symmetries

# The Fractional Quantum Hall Effect

Given the knowledge of integer quantum Hall effect, we now come to an
understanding of fractional quantum Hall effect. Indeed, the above
argument being relavent with topology has a loophole and ultimately they
hold only for non-interacting particles.

## The Laughlin Wavefunction

The very first attmept made by physicist was Laughlin in 80' that he
proposed an exact form of multi-particle wavefunction and obtained the
fractional Laudau level, 

$$

    \nu = \frac{1}{m}, \quad , m\in\mathbb{Z}

$$ 

Actually, $m$ is an odd integer due to the Fermi-Dirac
statistics. As we see from solving the single-particle wavefunction at
each Laudau level, the wavefunction may take the following form when
working in the symmetric gauge 

$$

    \psi(z_1,\ldots,z_n)= f(z_1,\ldots,z_n)e^{-\sum_{i=1}^N |z_i|^2/4l_B^2}

$$ 

where $z_i$ is defined as the holomorphic coordinate
for each particle. Laughlin proposed that the ground state wavefunction
for Laudau level $\nu=\frac{1}{m}$ is: 

$$

    \psi(z_i) = \prod_{i<j}(z_i-z_j)^m e^{-\sum_{i=1}^N |z_i|^2/4l_B^2}

$$ 

This is anti-symmetric when $m$ is odd. For even $m$,
this can be seen as the model for quantum Hall effect for bosons.

We can use some approximation to see that this function indeed give rise
to a fractional Laudau level. Let us focus on one single particle, say
$z_1$. Then in the pre-factor, terms containing $z_1$ are

$$

    \prod_{i=1}^N(z_1-z_i)^m \sim z_1^{m(N-1)}

$$ 

Thus from what we see from the single-particle
wavefunction, particles now living within the maximum radius of
$R\approx\sqrt{2mN}l_B$. And this implies an area of
$A=\pi R^2 = 2\pi mNl_B^2$. Each Laudau level contains $AB/\Phi_0=mN$.
So states only fill a fraction of Laudau level with 

$$

    \nu = \frac{1}{m}

$$ 

as we expected.

It is quite surprising that as one solve the Shrödinger numerically, the
Laughlin wavefunction matches with it perfectly. However, there is no
reason for us to believe this would match when there are $10^{11}$
particles. Instead, we could think that this wavefucntion lives in the
same *universality class* as the true ground state.

#### Plasma analogy

We would like to give another physical picture for the Laughlin
wavefunction. Consider the number density in the ground state, which is
given by computing the expectation value of 

$$

    n(z) = \sum_{i=1}^N \delta(z-z_i)

$$ 

And this is given by 

$$

    \langle n(z)\rangle = \frac{\int \prod_{i=1}^N d^2z_i n(z) |\psi(z_i)|^2}{\int \prod_{i=1}^N d^2z_i |\psi(z_i)|^2}

$$ 

Here we can interpret it as computing the partition
function of a classical plasma, where the partition function is defined
by 

$$

    Z = \int \prod_{i=1}^N d^2z_i |\psi(z_i)|^2 = \int \prod_{i=1}^N d^2z_i \prod_{i<j} |z_i-z_j|^{2m} e^{-\sum_{i=1}^N |z_i|^2/2l_B^2}

$$ 

However for future convenience and a better physical
picture, we should introduce a factor for normalization to make the
integrand dimensionless, that is 

$$

    Z = \int \prod_{i=1}^N d^2z_i \prod_{i<j} \left|\frac{z_i-z_j}{l_B}\right|^{2m} e^{-\sum_{i=1}^N |z_i|^2/2l_B^2}

$$ 

In the usual computation of partition function, the
integrand is given by $e^{-\beta H}$, so here we can identify the
effective Hamiltonian as 

$$

    \beta H = -2m \sum_{i<j} \log\left|\frac{z_i-z_j}{l_B}\right| + \sum_{i=1}^N \frac{|z_i|^2}{2l_B^2}

$$ 

The first term can be interpreted as the Coulomb
interaction between particles in 2d space, while the second term can be
interpreted as a confining potential. If we set $\beta = \frac{2}{m}$,
then the effective Hamiltonian is given by 

$$

    H = -m^2 \sum_{i<j} \log\left|\frac{z_i-z_j}{l_B}\right| + \sum_{i=1}^N \frac{m}{4l_B^2}|z_i|^2

$$ 

where each single particle carries a charge $m$. One
can easily check that the second term is the interaction of particles
with a uniform background with charge density
$\rho_B = -\frac{1}{2\pi l_B^2}$. To minimize the energy, particles
would like to spread out in the space and neutralize the background
charge. Thus we have a particle density of $n = \frac{1}{2\pi m l_B^2}$,
which is exactly the same as what we have found before.

## Excitation states: quasi-holes and qusi-particles

To this end, we have already discussed the ground state of $\nu=1/m$
quantum Hall systems but not their excitations. Now we consider
quasi-hole excitations and their wave functions, which are easily
constructed. On the other hand, we would not discuss quasi-particle wave
functions since they have not been exactly shown in the literature in a
simple way.

The wave function for a quasi-hole excitation at position
$\eta \in \mathbb{C}$ is given by 

$$

    \psi(z_i) = \prod_{i=1}^N (z_i-\eta) \prod_{k<l}(z_k-z_l)^m e^{-\sum_{i=1}^N |z_i|^2/4l_B^2}

$$ 

If there are $M$ quasi-hole excitations at positions
$\eta_1,\ldots,\eta_M$, the wave function is given by 

$$

    \psi(z_i) = \prod_{i=1}^N \prod_{j=1}^M (z_i-\eta_j) \prod_{k<l}(z_k-z_l)^m e^{-\sum_{i=1}^N |z_i|^2/4l_B^2}

$$ 

A heuristic way to understand that the quasi-hole
carries a charge of $\frac{e}{m}$ is that we could place $m$ quasi-holes
at the same position $\eta$, where we have defined that electrons carry
a charge of $-e$. The wave function in this case is given by

$$

    \psi(z_i) = \prod_{i=1}^N (z_i-\eta)^m \prod_{k<l}(z_k-z_l)^m e^{-\sum_{i=1}^N |z_i|^2/4l_B^2}

$$ 

which is exactly the same as the original Laughlin wave
function with an additional electron at position $\eta$ if we promote
$\eta$ to be a dynamical variable. However, $\eta$ is just a parameter
in
[\[eq:quasi_hole_single\]](#eq:quasi_hole_single){reference-type="eqref"
reference="eq:quasi_hole_single"} and
[\[eq:quasi_hole_m\]](#eq:quasi_hole_m){reference-type="eqref"
reference="eq:quasi_hole_m"}, thus they have a fractional charge of
$\frac{e}{m}$.

## Topology behind fractional quantum Hall effect

In the first section [4](#sec:IQHE){reference-type="ref"
reference="sec:IQHE"}, we have already relate the integer quantum Hall
effect with its deeply hidden topology. A natural question is whether we
can also find the topological nature of fractional quantum Hall effect.
The two stories are quite different as we have already seen. But the
answer should certainly be yes and we will give a brief discussion here.

Let us first discuss the statistics of quantum particles in 2d space. In
the usual 3d space, we have two types of particles in quantum mechanics,
bosons and fermions, which pick up a phase of $1$ and $-1$ when we
exchange two identical particles, respectively. However, in 2d space, we
can have more general statistics, which is called *anyonic statistics*.
That is, when we exchange two identical particles, the wave function
would pick up a phase of $e^{i\theta}$ where $\theta$ can be any value
in $[0,2\pi)$.

Consider two identical particles rotate in two different directions. In
the first case they exchange positions twice in an anti-clockwise
direction. In the second case in a clockwise direction. If one inspect
their worldlines, one would find that the two configurations could not
be continuously deformed from one to the other. That is, although the
molulus square is the same, the wave function may have a memory from
what they experienced. 

$$

    \psi(\mathbf{r_1},\mathbf{r_2}) = e^{i\theta}\psi(\mathbf{r_2},\mathbf{r_1})

$$ 

where $\theta$ is not required to be $0$ or $\pi$,
instead it can be any value in $[0,2\pi)$. This is so called *quantum
statistics* or *fractional statistics*.

## Further results

There are other fractions that are not of the form $\nu=\frac{1}{m}$
found in experiements. They can be understood in a similar manner from
previous discussion.

# Quantum Hall Effect From Chern-Simons Theory

In this section, I briefly summarize how can we get quantum Hall effect
from a field theory view. We integrate over all degrees of freedom and
are left with external gauge fields $A_\mu$ and emergent gauge fields
$a_\mu$. The lowest order allowed in $2+1 d$ is given by Chern-Simons
term.

## Integer Quantum Hall Effect

We first investigate how to describe integer quantum Hall effect using
Chern-Simons theory. It is assumed that we integrate over all internal
degrees of freedom and only an effective action for $A_\mu$ is left. We
assume that translation symmetry and rotation symmetry are still
preserved, however parity and time reversal symmetry are both broken. As
we are now in $2+1 d$ spacetime, the lowest order term is given by
Chern-Simons term 

$$

    S_{\text{CS}} = \frac{k}{4\pi}\int d^3x A\wedge dA = \frac{k}{4\pi}\int d^3x \epsilon^{\mu\nu\rho}A_{\mu}\partial_\nu A_{\rho}

$$ 

Then the electromagnetic current is given by varying
the action with respect to the field, 

$$

    J^\mu = \frac{\delta S}{\delta A_\mu} = \frac{k}{2\pi} \epsilon^{\mu\nu\rho}\partial_\nu A_{\rho}

$$ 

where current conservation is satisfied automatically.
The time component is given by 

$$

    J^0 = \frac{k}{2\pi} \epsilon^{0\nu\rho}\partial_\nu A_{\rho} = \frac{k}{2\pi}B.

$$ 

that is, if we add external magnetic field on the
material, there would be induced charge from the magnetic field. At the
same time, spatial components are computed by

$$

    J^i = \frac{k}{2\pi} \epsilon^{ij}E_j

$$ 

and Hall conductivity is easily read from above
equation 

$$

    \sigma_{xy} = \frac{k}{2\pi}

$$ 

Up to now we haven't shown why this is quantized, which
needs a more careful study of self-consistence of Chern-Simons theory.
Firstly, we want this theory to be gauge-invariant. Let
$A_\mu\to A_\mu + \partial_\mu\omega$, then the variation of the action is 

$$

    S_{\text{CS}} \to S_{\text{CS}} + \frac{k}{4\pi} \int d\omega\wedge dA = S_{\text{CS}} + \frac{k}{4\pi} \int d(\omega\wedge dA).

$$ 

The boundary term vanishes if we put overselves on a
non-compact spacetime and consider transform near identity, which mean
$\omega(x)\to 0$ as $x\to\infty$. However if this is considered to be a
partition function with periodicity $\beta$, we may introduce *large
gauge transformations*. Now $\omega$ is nolonger required to be
single-valued, we only want $e^{ie\omega/\hbar}$ to be single-valued as
one move from $\tau=0\to\tau=\beta$. This implies a holonomy in $S^1$
time direction is possible 

$$

    \omega = \frac{2\pi\hbar\tau}{e\beta}.

$$ 

And $A_0$ can be thought as a periodic variable with
periodicity $\frac{2\pi\hbar}{e\beta}$. Apart from time direction, we
could also make the spatial directions compact, that is $\mathbf{S}^2$
instead of $\mathbf{R}^2$. And a background magnetic flux is imposed,

$$

    \frac{1}{2\pi}\int_{\mathbf{S}^2}dA = \frac{\hbar}{e}

$$ 

If we assume a constant $A_0=a$, then Chern-Simons
action is calculated easily 

$$

    S_{\text{CS}} = \frac{k}{2\pi} \int d^3x A_0F_{12} = \frac{ka\beta\hbar}{e}

$$ 

while $e^{iS_{\text{CS}}/\hbar}$ is required to be
single-valued as $A_0\to A_0+ \frac{2\pi\hbar}{\beta e}$, thus

$$

    \frac{k\hbar}{e^2} = \nu\in \mathbf{Z}

$$ 

In all, the Hall conductivity is required to be
quantized 

$$

    \sigma_{xy} = \frac{e^2}{2\pi\hbar}\nu

$$

## Fractional Quantum Hall Effect

As we move from the first full filling Laudau level to partial filling
Laudau level, there the low-energy physics should be treated more
carefully. We can no longer assume all bulk degrees of freedom are
integrated out, however, some of them must be collected to form a new
topological degree of freedom, that is, we have an emergent gauge field
$a_\mu$.

The goal is to write down the effective action
$S_{\text{eff}}[a_\mu,A_\mu]$. And we want to couple those two different
gauge fields. As what we did in the former subsection, following form of
current is possible 

$$

    J^\mu = \frac{1}{2\pi} \epsilon^{\mu\nu\rho}\partial_\nu a_{\rho}

$$ 

Then if we include both the dynamics of emergent field
and coupling with external field, the action is given by

$$

    S_{\text{eff}}[a_\mu,A_\mu] = \int d^3x \frac{1}{2\pi}A\wedge da - \frac{m}{4\pi} A\wedge dA

$$
