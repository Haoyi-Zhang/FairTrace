"""Direct vector diagrams for the declared reset contracts and canonical graphs."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyArrowPatch

plt.rcParams.update({'font.family':'STIXGeneral','mathtext.fontset':'stix',
                     'font.size':8.5,'pdf.fonttype':42,'ps.fonttype':42,
                     'text.usetex':False,'axes.unicode_minus':False})


class Drawing:
    def __init__(self,w,h):
        self.fig=plt.figure(figsize=(w/2.54,h/2.54))
        self.ax=self.fig.add_axes([0,0,1,1],xlim=(0,w),ylim=(0,h))
        self.ax.set_aspect('equal');self.ax.axis('off');self.labels=[]

    def text(self,x,y,s,size=8.5):
        self.labels.append(self.ax.text(x,y,s,ha='center',va='center',
                          fontsize=size,linespacing=1.15,zorder=4))

    def box(self,x,y,w,h,s='',circle=False,dashed=False):
        p=Circle((x,y),w/2) if circle else Rectangle((x-w/2,y-h/2),w,h)
        p.set(edgecolor='black',facecolor='white',lw=.65,zorder=2,
              linestyle='--' if dashed else '-')
        self.ax.add_patch(p)
        if s:self.text(x,y,s)

    def line(self,points,arrow=False,dashed=False):
        x,y=zip(*points);self.ax.plot(x,y,color='black',lw=.65,
                                   ls='--' if dashed else '-',zorder=1)
        if arrow:self.curve(points[-2],points[-1],0)

    def curve(self,start,end,rad):
        self.ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',
                           connectionstyle=f'arc3,rad={rad}',mutation_scale=8,
                           color='black',lw=.65,zorder=1))

    def save(self,out,name):
        self.fig.canvas.draw();renderer=self.fig.canvas.get_renderer();extent=self.fig.bbox
        for label in self.labels:
            b=label.get_window_extent(renderer)
            if b.x0<extent.x0 or b.x1>extent.x1 or b.y0<extent.y0 or b.y1>extent.y1:
                raise ValueError('Clipped label: '+label.get_text())
        self.fig.savefig(out/(name+'.pdf'),metadata={'Creator':'Python Matplotlib',
                         'Producer':None,'CreationDate':None,'ModDate':None})
        plt.close(self.fig)


def regular(out):
    d=Drawing(12.4,5.5)
    for x,s,w in [(1.6,'Annotated input\n$x\\in\\Sigma^\\omega$\n$\\chi(x)$',2.8),
                  (6.2,'Finite-state expander\n$T=(Q,q_0,\\delta,\\lambda)$',3.0),
                  (10.8,'Target word\n$T(x)\\in\\{0,1\\}^\\omega$',2.8)]:
        d.box(x,4.1,w,1.35,s)
    d.line([(3.0,4.1),(4.7,4.1)],arrow=True)
    d.line([(7.7,4.1),(9.4,4.1)],arrow=True)
    d.text(3.85,4.85,'Edge\nclasses',8)
    d.text(8.55,4.85,'Nonempty\nblocks',8)
    d.line([(1.6,3.425),(1.6,2.7)],arrow=True)
    d.line([(10.8,3.425),(10.8,2.7)],arrow=True)
    d.text(1.6,2.18,'Source accepted\niff $x\\in\\mathcal{F}_{B,a}^{\\chi}$')
    d.text(10.8,2.18,'Target demand\n$\\mathrm{gap}_t(T(x))$')
    d.box(6.2,.85,5.8,1.2,'Exact target bounds\n$\\mathsf{U}_T(B,a,t)\\leq C<\\mathsf{R}_T(B,a,t)$')
    d.line([(1.6,1.7),(3.3,1.35)],arrow=True)
    d.line([(10.8,1.7),(9.1,1.35)],arrow=True)
    d.save(out,'regular-interface')


def phase(out):
    d=Drawing(12.4,4.2)
    d.text(.64,3.3,'Initial');d.text(.64,1.55,'Interior')
    for x,w,s,dash in [(1.9,.55,'$t$',True),(3.4,2.0,'$d k_0$ misses',False),
                        (4.95,.65,'$p$',False),(5.6,.45,'$0$',False)]:
        d.box(x,3.3,w,.65,s,dashed=dash)
    d.text(9.0,3.3,'$t+d k_0+p\\leq C$')
    for x,w,s in [(1.9,.45,'$0$'),(2.6,.7,'$q$'),(4.1,2.0,'$d k_j$ misses'),
                  (5.65,.65,'$p$'),(6.3,.45,'$0$')]:
        d.box(x,1.55,w,.65,s)
    d.text(9.75,1.55,'$q+d k_j+p\\leq C$')
    for left,right,s in [(1.675,2.95,'End of $u$'),(5.325,6.525,'Start of next $u$')]:
        d.line([(left,1.13),(left,.98),(right,.98),(right,1.13)])
        d.text((left+right)/2,.69,s,8)
    d.text(6.2,.19,'Dashed box: initial counter state, not an emitted event.',8)
    d.save(out,'phase-contract')


def microstep(out):
    d=Drawing(12.4,4.8)
    d.box(1.15,3.7,1.8,.72,'$v$');d.box(11.25,3.7,1.8,.72,"$v'$")
    d.line([(2.05,3.7),(10.35,3.7)],arrow=True)
    d.text(6.2,4.3,'$e:\\ (\\chi_E(e),\\ell(e))$',9)
    d.box(1.15,1.9,1.8,.72,'$(v,q)$')
    for x,s in [(3.8,'$1$'),(6.2,'$\\cdots$'),(8.6,'$k-1$')]:
        size=.95 if x==8.6 else .62
        d.box(x,1.9,size,size,s,circle=True)
    d.box(11.25,1.9,1.8,.72,"$(v',q')$")
    for left,right,label in [(2.05,3.49,'$b_0,\\epsilon$'),(4.11,5.89,'$b_1,\\epsilon$'),
                              (6.51,8.125,'$b_{k-2},\\epsilon$'),(9.075,10.35,'$b_{k-1},\\ell(e)$')]:
        d.line([(left,1.9),(right,1.9)],arrow=True)
        d.text((left+right)/2,2.4,label,8)
    d.text(6.2,.66,"$q'=\\delta(q,\\eta(e))$; $b_0\\cdots b_{k-1}=\\lambda(q,\\eta(e))\\ne\\epsilon$",8.5)
    d.save(out,'microstep')


def viability(out):
    d=Drawing(12.4,4.5)
    d.box(1.0,2.65,.68,.68,'$s$',circle=True)
    d.curve((.78,2.9),(1.22,2.9),-2.2)
    d.curve((1.22,2.4),(.78,2.4),-2.2)
    d.text(1.0,3.8,'$a$');d.text(1.0,1.48,'$b$')
    d.text(1.0,.52,'Raw product')
    d.box(4.0,2.65,1.35,.72,'$(0,0)$')
    d.line([(1.6,2.65),(3.325,2.65)],arrow=True)
    d.text(2.47,3.2,'$B=0$');d.text(4.0,.52,'No retained edge')
    d.line([(5.6,.2),(5.6,4.1)],dashed=True)
    d.box(7.0,2.65,1.35,.72,'$(0,0)$')
    d.box(10.2,3.4,1.35,.72,'$(0,1)$')
    d.box(10.2,1.9,1.35,.72,'$(1,0)$')
    d.line([(7.675,2.82),(9.525,3.4)],arrow=True)
    d.line([(7.675,2.48),(9.525,1.9)],arrow=True)
    d.text(8.48,3.43,'$a$');d.text(8.48,1.87,'$b$')
    d.curve((9.8,3.04),(9.8,2.26),.38)
    d.curve((10.6,2.26),(10.6,3.04),.38)
    d.text(9.32,2.65,'$b$');d.text(11.08,2.65,'$a$')
    d.text(8.9,.52,'$B=1$: alternating continuation')
    d.save(out,'viability')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--outdir',type=Path,default=Path(__file__).resolve().parent)
    out=parser.parse_args().outdir;out.mkdir(parents=True,exist_ok=True)
    for draw in (regular,phase,microstep,viability):draw(out)
