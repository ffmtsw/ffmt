Transfer Function container (mt)
==========================

Purpose
-------

``mt`` is a MATLAB struct that stores site-specific magnetotelluric (MT) transfer functions, derived tensors, and processing metadata. It is produced by ``allocate_mt(mode)`` and consumed by FFMT plotting/mapping/modeling tools.

Quick start
-----------

.. code-block:: matlab

   % Create an empty site container
   mt = allocate_mt();

   % Minimum fields to start filling
   mt.site   = 'OL01';
   mt.lonlat = [35.9850, -2.7690];   % [lon, lat] WGS84 (deg)
   mt.z      = 2450;                 % elevation (m)

   % Define frequency vector (Hz) and periods (s)
   mt.freq  = logspace(-3, 3, 80).';  % column vector [N×1]
   mt.per   = 1 ./ mt.freq;           % keep both for convenience
   mt.nfreq = numel(mt.freq);

   % Set units and conventions explicitly via mt.info
   mt.info.date    = string(datetime('today','Format','dd-MM-yyyy'));
   mt.info.E.unit  = 'mV/km';         % electric field unit (example)
   mt.info.B.stat  = true;            % using B (flux density)
   mt.info.B.unit  = 'nT';
   mt.info.H.stat  = false;           % not using H
   mt.info.Z.unit  = 'mV/km/nT';      % Z unit consistent with E/B
   mt.info.source  = 'processing';    % 'edi' | 'processing' | 'ModEM' | ...

   % Allocate impedance and errors (N×1 vectors per component)
   N = mt.nfreq;
   [mt.Zxx, mt.Zxy, mt.Zyx, mt.Zyy] = deal(complex(zeros(N,1)));
   [mt.Zxx_Err, mt.Zxy_Err, mt.Zyx_Err, mt.Zyy_Err] = deal(zeros(N,1));

   % (Optional) derived quantities — set when available
   [mt.rhoxy, mt.rhoyx] = deal(zeros(N,1));
   [mt.phixy, mt.phiyx] = deal(zeros(N,1));   % degrees
   [mt.txz, mt.tyz]     = deal(complex(zeros(N,1)));

Field reference (top-level)
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 24 14 40

   * - Field
     - Type / Shape
     - Units
     - Description
   * - site
     - char or string
     - —
     - Site identifier (code).
   * - info
     - struct
     - —
     - Metadata: date, units, rotations, source, processing (see below).
   * - lonlat
     - double [1×2]
     - deg
     - Geographic coordinates [lon, lat] (WGS84).
   * - UTM
     - double [1×2]
     - m
     - Projected coordinates [X, Y] (zone/datum documented in ``info``).
   * - XY
     - double [1×2]
     - km
     - Local reference [X, Y] relative to dataset center.
   * - z
     - double
     - m
     - Elevation (positive above mean sea level).
   * - nfreq
     - integer
     - —
     - Number of evaluated frequencies.
   * - freq
     - double [N×1]
     - Hz
     - Evaluated frequencies.
   * - per
     - double [N×1]
     - s
     - Evaluated periods.

Impedance, apparent resistivity, phase, tippers
-----------------------------------------------

Each component is stored as an **N×1** vector. Error fields use the suffix ``*_Err`` and have the **same shape**.

.. list-table::
   :header-rows: 1
   :widths: 20 22 14 44

   * - Field(s)
     - Type / Shape
     - Units
     - Notes
   * - Zxx, Zxy, Zyx, Zyy
     - complex double [N×1]
     - per ``mt.info.Z.unit``
     - Impedance tensor components.
   * - Zxx_Err, Zxy_Err, Zyx_Err, Zyy_Err
     - double [N×1]
     - Z units
     - Associated errors (definition depends on your pipeline).
   * - rhoxx, rhoxy, rhoyx, rhoyy
     - double [N×1]
     - Ω·m
     - Apparent resistivity tensor components.
   * - rhoxx_Err, rhoxy_Err, rhoyx_Err, rhoyy_Err
     - double [N×1]
     - Ω·m
     - Associated errors.
   * - phixx, phixy, phiyx, phiyy
     - double [N×1]
     - °
     - Impedance phase (atan2(Im(Z), Re(Z))).
   * - phixx_Err, phixy_Err, phiyx_Err, phiyy_Err
     - double [N×1]
     - °
     - Associated errors.
   * - txz, tyz
     - complex double [N×1]
     - —
     - Tippers (Txz, Tyz).
   * - txz_Err, tyz_Err
     - double [N×1]
     - —
     - Associated errors.

Phase Tensor (Φ), Resistivity Tensors (real/imag) and RPT
---------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 22 12 44

   * - Field(s)
     - Type / Shape
     - Units
     - Notes
   * - phi11, phi12, phi21, phi22 (+ *_Err)
     - double [N×1]
     - —
     - Phase Tensor components (dimensionless; angles in ° for eigenterms below).
   * - phimax, phimin, alpha, beta (+ *_Err)
     - double [N×1]
     - °
     - PT eigen-angles and skew parameters.
   * - rt11, rt12, rt21, rt22 (+ *_Err)
     - double [N×1]
     - Ω·m
     - Real resistivity tensor.
   * - resreal_max, resreal_min, resreal_alpha, resreal_beta (+ *_Err)
     - double [N×1]
     - Ω·m / °
     - Eigen-values/angles for real resistivity tensor.
   * - irt11, irt12, irt21, irt22 (+ *_Err)
     - double [N×1]
     - Ω·m
     - Imaginary resistivity tensor.
   * - resimag_max, resimag_min, resimag_alpha, resimag_beta (+ *_Err)
     - double [N×1]
     - Ω·m / °
     - Eigen-values/angles for imaginary resistivity tensor.
   * - rpt11, rpt12, rpt21, rpt22 (+ *_Err)
     - double [N×1]
     - °
     - Resistivity Phase Tensor (angles in degrees for eigenterms below).
   * - resphase_max, resphase_min, resphase_alpha, resphase_beta (+ *_Err)
     - double [N×1]
     - °
     - Eigen-angles for RPT.

``mt.info`` (metadata)
----------------------

.. code-block:: text

   info.date           : string, assignment date (e.g., '02-10-2025')
   info.E.unit         : string, e.g., 'mV/km'
   info.E.rot          : numeric (deg), rotation applied to E
   info.B.stat         : logical, true if B (flux density) is used
   info.B.unit         : string, e.g., 'nT'
   info.B.rot          : numeric (deg), rotation applied to B
   info.H.stat         : logical, true if H (magnetic field) is used
   info.H.unit         : string, e.g., 'A/m'
   info.H.rot          : numeric (deg), rotation applied to H
   info.Z.unit         : string, e.g., 'mV/km/nT' or 'Ohm'
   info.Z.rot          : numeric or text, rotation convention (+CW / -CCW)
   info.staticshift.xx : numeric, per-component scaling (optional)
   info.staticshift.xy : numeric, ...
   info.staticshift.yx : numeric, ...
   info.staticshift.yy : numeric, ...
   info.staticshift.xz : complex, for txz
   info.staticshift.yz : complex, for tyz
   info.source         : string, origin: 'edi' | 'processing' | 'ModEM' | ...
   info.processing     : struct with: software, version, mode, job, rem_ref, rem_site, distance

Sanity checks
-------------

.. code-block:: matlab

   function check_mt_shape(mt)
       N = mt.nfreq;
       assert(size(mt.freq,1) == N, 'freq must be [N×1]');
       assert(size(mt.per,1)  == N, 'per must be [N×1]');
       comps = {'Zxx','Zxy','Zyx','Zyy','txz','tyz', ...
                'rhoxx','rhoxy','rhoyx','rhoyy', ...
                'phixx','phixy','phiyx','phiyy'};
       for k = 1:numel(comps)
           if ~isempty(mt.(comps{k}))
               assert(isequal(size(mt.(comps{k})), [N,1]), ['Bad shape: ', comps{k}]);
           end
           efield = [comps{k},'_Err'];
           if isfield(mt, efield) && ~isempty(mt.(efield))
               assert(isequal(size(mt.(efield)), [N,1]), ['Bad shape: ', efield]);
           end
       end
   end

Common pitfalls
---------------

- **Z definition (E/B vs E/H)**: Be explicit. If Z is from E/B, ensure ``mt.info.Z.unit`` matches your μ₀ scaling choice—do not mix conventions silently.
- **Column vectors only**: Keep ``[N×1]`` consistently.
- **Angles in degrees**: Store and label as degrees.
